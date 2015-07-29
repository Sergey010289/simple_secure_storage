import base64
import os
from Crypto.Cipher import AES
from django.db import models
from django.utils import six
from django.utils.encoding import smart_text
from simple_secure_storage.settings import BLOCK_SIZE

__author__ = 'smuravko'

secret = os.urandom(BLOCK_SIZE)


class EncryptedAESCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.padding_symbol = '{'
        self.cipher = AES.new(secret)

        if 'max_length' in kwargs.keys():
            kwargs['max_length'] = len(base64.b64encode(
                os.urandom(kwargs['max_length'])))

        super(EncryptedAESCharField, self).__init__(*args, **kwargs)

    def to_python(self, value, *args, **kwargs):
        if isinstance(value, six.string_types) or value is None:
            if value:
                pad = lambda s: \
                    s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * self.padding_symbol
                encode_aes = lambda c, s: base64.b64encode(c.encrypt(pad(s)))    # TODO: need relocate from here
                return encode_aes(self.cipher, value)
            else:
                return value

        return smart_text(value)

    def get_prep_value(self, value):
        value = super(EncryptedAESCharField, self).get_prep_value(value)

        if value:
            return self.to_python(self._decode_aes(self.cipher, value))
        return self.to_python(value)

    def _decode_aes(self, cipher, encoded_string):
        enc_str = base64.urlsafe_b64decode(encoded_string)
        decrypted_string = cipher.decrypt(enc_str)
        return decrypted_string.decode('utf8').rstrip(self.padding_symbol)

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value


class EncryptedAESEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        self.padding_symbol = '_'
        self.cipher = AES.new(secret)
        kwargs['max_length'] = kwargs.get('max_length', 254)
        super(EncryptedAESEmailField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        print('--> to python')
        if isinstance(value, six.string_types) or value is None:
            if value:
                pad = lambda s: \
                    s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * self.padding_symbol
                EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))    # TODO: need relocate from here
                return EncodeAES(self.cipher, value)
            else:
                return value

        return smart_text(value)

    def get_prep_value(self, value):
        value = super(EncryptedAESEmailField, self).get_prep_value(value)

        if value:
            return self.to_python(self._decode_aes(self.cipher, value))
        return self.to_python(value)

    def _decode_aes(self, cipher, encoded_string):
        enc_str = base64.urlsafe_b64decode(encoded_string)
        decrypted_string = cipher.decrypt(enc_str)
        return decrypted_string.decode('utf8').rstrip(self.padding_symbol)

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value
