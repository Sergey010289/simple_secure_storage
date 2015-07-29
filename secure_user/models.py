import os
import base64
from Crypto.Cipher import AES
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from documents.encryption import EncryptWithAES, DecryptWithAES
from secure_user.managers import CustomUserManager
from simple_secure_storage.settings import BLOCK_SIZE, IV

__author__ = 'smuravko'
_app_label = 'secure_user'


class User(models.Model):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.store_fields = ['first_name', 'last_name']
        if self.id:
            self._get_original_state()

    email = models.EmailField(
        unique=True, db_index=True, blank=False, null=False)
    password = models.CharField(max_length=80, blank=False, null=False)
    _first_name = models.CharField(
        max_length=255, db_column='first_name', blank=True, null=True)
    _last_name = models.CharField(
        max_length=255, db_column='last_name', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = CustomUserManager()

    class Meta(AbstractUser.Meta):
        app_label = _app_label
        swappable = 'AUTH_USER_MODEL'

    @property
    def first_name(self):
        if self._first_name:
            secret_key = base64.b64decode(self.get_key())
            cipher_for_decryption = AES.new(secret_key, AES.MODE_CBC, IV)
            return DecryptWithAES(cipher_for_decryption, self._first_name)

    @first_name.setter
    def first_name(self, value):
        secret_key = base64.b64decode(self.get_key(self.pk))
        cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
        self._first_name = self._encrypt_value(
            cipher_for_encryption, value)

    @property
    def last_name(self):
        if self.last_name:
            secret_key = base64.b64decode(self.get_key())
            cipher_for_decryption = AES.new(secret_key, AES.MODE_CBC, IV)
            return DecryptWithAES(cipher_for_decryption, self._last_name)

    @last_name.setter
    def last_name(self, value):
        secret_key = base64.b64decode(self.get_key(self.pk))
        cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
        self._last_name = self._encrypt_value(
            cipher_for_encryption, value)

    @staticmethod
    def _encrypt_value(cipher, field_name):
        return EncryptWithAES(cipher, field_name)

    def _get_original_state(self):
        secret_key = base64.b64decode(self.get_key())
        self.__original_state = {}
        for i in self.store_fields:
            cipher_for_decryption = AES.new(secret_key, AES.MODE_CBC, IV)
            self.__original_state[i] = DecryptWithAES(cipher_for_decryption, getattr(self, '_%s' % i))

    def save(self, update_fields=None, *args, **kwargs):
        print('SAVE!!!')

        if self.pk:

            print('origin before: ', self.__original_state)
            #
            super(User, self).save(*args, **kwargs)
        else:
            print('creating key')
            secret_key = os.urandom(BLOCK_SIZE)

            cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
            self._first_name = EncryptWithAES(
                cipher_for_encryption, self._first_name)

            cipher_for_encryption = AES.new(secret_key, AES.MODE_CBC, IV)
            self._last_name = EncryptWithAES(
                cipher_for_encryption, self._last_name)

            super(User, self).save(*args, **kwargs)
            self.set_key(base64.b64encode(secret_key).decode('utf-8'))

        self._get_original_state()
        print('origin after: ', self.__original_state)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def set_key(self, key):
        UserRemoteKey.objects.db_manager('remote_storage').create(**{
            'user': self,
            'key': key
        })

    def get_key(self, pk=None):
        if pk:
            return UserRemoteKey.objects.db_manager('remote_storage').get(
                user=pk).key
        return UserRemoteKey.objects.db_manager('remote_storage').get(
            user=self).key

    def check_password(self, password):
        return check_password(password, self.password)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __str__(self):
        return self.email


class UserRemoteKey(models.Model):
    user = models.ForeignKey(User, related_name='remote_key')
    key = models.CharField(max_length=BLOCK_SIZE)

    class Meta:
        app_label = _app_label