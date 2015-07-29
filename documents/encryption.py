import os
from simple_secure_storage.settings import BLOCK_SIZE, INTERRUPT, PAD, IV
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

__author__ = 'smuravko'


def AddPadding(data, interrupt, pad, block_size):
    print('add padding')
    # print(type(data))
    if not isinstance(data, str):
        data = data.decode('utf8')
    new_data = ''.join([data, interrupt])
    new_data_len = len(new_data)
    remaining_len = block_size - new_data_len
    to_pad_len = remaining_len % block_size
    pad_string = pad * to_pad_len
    return ''.join([new_data, pad_string])


def StripPadding(data, interrupt, pad):
    return data.decode('utf8', 'ignore').rstrip(pad).rstrip(interrupt)

import base64
# SECRET_KEY = u'a1b2c3d4e5f6g7h8a1b2c3d4e5f6g7h8'
# SECRET_KEY = os.urandom(32)



# cipher_for_encryption = AES.new(SECRET_KEY, AES.MODE_OFB, IV)
# cipher_for_decryption = AES.new(SECRET_KEY, AES.MODE_OFB, IV)
# cipher_for_encryption = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
# cipher_for_decryption = AES.new(SECRET_KEY, AES.MODE_CBC, IV)


def EncryptWithAES(encrypt_cipher, plaintext_data):
    plaintext_padded = AddPadding(plaintext_data, INTERRUPT, PAD, BLOCK_SIZE)
    encrypted = encrypt_cipher.encrypt(plaintext_padded)
    return b64encode(encrypted)


def DecryptWithAES(decrypt_cipher, encrypted_data):
    decoded_encrypted_data = b64decode(encrypted_data)
    decrypted_data = decrypt_cipher.decrypt(decoded_encrypted_data)
    return StripPadding(decrypted_data, INTERRUPT, PAD)


# our_data_to_encrypt = 'qwet'
# encrypted_data = EncryptWithAES(cipher_for_encryption, our_data_to_encrypt)
# print('Encrypted string:', encrypted_data)
# print('Encrypted string:', encrypted_data.decode('utf8'))
#
# # And let's decrypt our data
# decrypted_data = DecryptWithAES(cipher_for_decryption, encrypted_data)
# print('Decrypted string:', decrypted_data)
