import base64
from Crypto.Cipher import AES
from django.db import models

from simple_secure_storage.settings import IV

from documents.encryption import DecryptWithAES, EncryptWithAES
from documents.managers import CustomDocumentManager
from documents.validators import validate_file

from secure_user.models import User, UserRemoteKey

__author__ = 'smuravko'
_app_label = 'documents'


class Document(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    file = models.FileField(upload_to='uploads/', validators=[validate_file], blank=True, null=True)
    _private_number = models.CharField(
        max_length=80, db_column='private_number', blank=True, null=True)
    _summary = models.CharField(
        max_length=255, db_column='summary', blank=True, null=True)

    objects = CustomDocumentManager()

    class Meta:
        app_label = _app_label

    @property
    def private_number(self):
        if self._private_number:
            secret_key = base64.b64decode(self.get_key(self.author.id))
            cipher_for_decryption = AES.new(secret_key, AES.MODE_CBC, IV)
            return DecryptWithAES(cipher_for_decryption, self._private_number)

    @private_number.setter
    def private_number(self, value):
        secret_key = base64.b64decode(self.get_key(self.author.id))
        cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
        self._private_number = self._encrypt_value(
            cipher_for_encryption, value)

    @property
    def summary(self):
        if self._summary:
            secret_key = base64.b64decode(self.get_key(self.author.id))
            cipher_for_decryption = AES.new(secret_key, AES.MODE_CBC, IV)
            return DecryptWithAES(cipher_for_decryption, self._summary)

    @summary.setter
    def summary(self, value):
        secret_key = base64.b64decode(self.get_key(self.author.id))
        cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
        self._summary = self._encrypt_value(
            cipher_for_encryption, value)

    def get_key(self, pk=None):
        if pk:
            return UserRemoteKey.objects.db_manager('remote_storage').get(
                user=pk).key
        return UserRemoteKey.objects.db_manager('remote_storage').get(
            user=self.author).key

    @staticmethod
    def _encrypt_value(cipher, field_name):
        return EncryptWithAES(cipher, field_name)

    def save(self, update_fields=None, *args, **kwargs):
        if not self.pk:
            secret_key = base64.b64decode(self.get_key(self.author.id))

            if self._private_number:
                cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
                self._private_number = EncryptWithAES(
                    cipher_for_encryption, self._private_number)

            if self._summary:
                cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
                self._summary = EncryptWithAES(
                    cipher_for_encryption, self._summary)

        super(Document, self).save(*args, **kwargs)

        self.permissions.get_or_create(**{
            'document': self,
            'user': self.author,
            'can_read': True,
            'can_update': True,
            'can_delete': True
        })


# PERMIT_CHOICES = (
#     ('R', 'Read'),
#     ('W', 'Write'),
#     ('D', 'Delete'),
# )
#


class DocumentPermission(models.Model):
    document = models.ForeignKey(Document, related_name='permissions')
    user = models.ForeignKey(User)
    # permit = models.CharField(
    #     max_length=1, choices=PERMIT_CHOICES, blank=False, null=False)
    can_read = models.BooleanField(default=False, blank=False, null=False)
    can_update = models.BooleanField(default=False, blank=False, null=False)
    can_delete = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        app_label = _app_label
        unique_together = ('document', 'user')
