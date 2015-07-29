# from cryptography.fernet import Fernet
# import base64
# import os
# # key = Fernet.generate_key()
# # key = base64.urlsafe_b64encode(os.urandom(32))
# print(os.urandom(32))
# key = base64.urlsafe_b64encode(b'2' * 32)
# f = Fernet(key)
# token = f.encrypt(b"my deep dark secret")
# print(token)
#
# q = f.decrypt(token)
# print(q)
 ###########
# from Crypto.Cipher import AES
# key = '0123456789' * 32
# IV = 16 * '\x00'           # Initialization vector: discussed later
# mode = AES.MODE_CBC
# encryptor = AES.new(key, mode, IV=IV)
#
# # text = 'j' * 64 + 'i' * 128
# text = b'xxx' * 100
# print(text)
# ciphertext = encryptor.encrypt(text)
# print(ciphertext)

 ############
#
# import base64
# from Crypto.Cipher import AES
# from Crypto import Random
#
# # key = '0123456789abcde1f'
# key = 16 * '\x00'
# print(key)
# print(len(key))
#
# BS = 16
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s : s[:-ord(s[len(s)-1:])]
#
#
# class AESCipher:
#     def __init__( self, key ):
#         self.key = key
#
#     def encrypt( self, raw ):
#         raw = pad(raw)
#         iv = Random.new().read( AES.block_size )
#         cipher = AES.new( self.key, AES.MODE_CBC, iv )
#         return base64.b64encode( iv + cipher.encrypt( raw ) )
#
#     def decrypt( self, enc ):
#         enc = base64.b64decode(enc)
#         iv = enc[:16]
#         cipher = AES.new(self.key, AES.MODE_CBC, iv )
#         return unpad(cipher.decrypt( enc[16:] ))
#
# q = AESCipher(key)
# print('------')
# test1 = '123'
# test2 = 'lsdfjskjlk21jlkj2 l1kj23lk1j3 lk12j'
# test1_cipher = q.encrypt(test1)
# print(len(test1), ' <-> ', len(q.encrypt(test1)))
# test2_cipher = q.encrypt(test2)
# print(len(test2), ' <-> ', len(q.encrypt(test2)))
#
# print('decrypt')
# print(q.decrypt(test2_cipher))
# qq = str(q.decrypt(test2_cipher))
# print(type(qq))
# print(qq)

# from Crypto.Cipher import AES
# import base64
# import os
#
# # the block size for the cipher object; must be 16, 24, or 32 for AES
# BLOCK_SIZE = 32
#
# # the character used for padding--with a block cipher such as AES, the value
# # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# # used to ensure that your value is always a multiple of BLOCK_SIZE
# PADDING = '{'
#
# # one-liner to sufficiently pad the text to be encrypted
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#
# # one-liners to encrypt/encode and decrypt/decode a string
# # encrypt with AES, encode with base64
# # EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
# EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
# DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))#.replace(PADDING, '')#.rstrip(PADDING)
#
# # generate a random secret key
# secret = os.urandom(BLOCK_SIZE)
#
# # create a cipher object using the random secret
# cipher = AES.new(secret)
#
# # encode a string
# encoded = EncodeAES(cipher, 'password')
# print('Encrypted string:', encoded)
#
# # decode the encoded string
#
# def DecodeAES(c, e):
#     cipher = c
#     encoded_string = e
#     enc_str = base64.urlsafe_b64decode(encoded_string)
#     decrypted_string = cipher.decrypt(enc_str)
#     return decrypted_string.decode('utf8').rstrip(PADDING)
# #
# # decoded = DecodeAES(cipher, encoded)
# # print('Decrypted string:', decoded)
# print(DecodeAES(cipher, encoded))


# from Crypto.Cipher import AES
# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message = "The answer is no"
# print(len('This is a key123'))
# print(len(message))
# ciphertext = obj.encrypt(message)
# print(ciphertext)
# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# print(obj2.decrypt(ciphertext))
# # print(ciphertext)


from Crypto.Cipher import AES
import base64
import os

# размер блока шифрования
BLOCK_SIZE = 32

# символ, использующийся для дополнения шифруемых данных
# до размера, кратного 32 байтам
PADDING = '{'

# функция дополнения
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# функции шифрования и расшифрования
# результат дополнительно обертывается в base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode('utf8').rstrip(PADDING)


def decode_aes(cipher, encoded_string):
    enc_str = base64.urlsafe_b64decode(encoded_string)
    decrypted_string = cipher.decrypt(enc_str)
    return decrypted_string.decode('utf8').rstrip(PADDING)
# генерируем ключ
secret = os.urandom(BLOCK_SIZE)

# создаем объект
cipher = AES.new(secret)

# шифруем строку
encoded = EncodeAES(cipher, 'password5559easdas')
# print('Encrypted string:', encoded)

# расшифровываем строку
decoded = decode_aes(cipher, encoded)
# print('Decrypted string:', decoded)

# расшифровываем строку
decoded = DecodeAES(cipher, encoded)
# print('Decrypted string:', decoded)



############

from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os
from datetime import datetime
from re import sub

# AES is a block cipher so you need to define size of block.
# Valid options are 16, 24, and 32
BLOCK_SIZE = 32

INTERRUPT = u'\u0001'
PAD = u'\u0000'

def AddPadding(data, interrupt, pad, block_size):
    new_data = ''.join([data, interrupt])
    new_data_len = len(new_data)
    remaining_len = block_size - new_data_len
    to_pad_len = remaining_len % block_size
    pad_string = pad * to_pad_len
    return ''.join([new_data, pad_string])

def StripPadding(data, interrupt, pad):
    return data.decode('utf8').rstrip(pad).rstrip(interrupt)

import base64
# SECRET_KEY = u'a1b2c3d4e5f6g7h8a1b2c3d4e5f6g7h8'
SECRET_KEY = os.urandom(32)

IV = u'12345678abcdefgh'

# cipher_for_encryption = AES.new(SECRET_KEY, AES.MODE_OFB, IV)
# cipher_for_decryption = AES.new(SECRET_KEY, AES.MODE_OFB, IV)
cipher_for_encryption = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
cipher_for_decryption = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

def EncryptWithAES(encrypt_cipher, plaintext_data):
    plaintext_padded = AddPadding(plaintext_data, INTERRUPT, PAD, BLOCK_SIZE)
    encrypted = encrypt_cipher.encrypt(plaintext_padded)
    return b64encode(encrypted)

def DecryptWithAES(decrypt_cipher, encrypted_data):
    decoded_encrypted_data = b64decode(encrypted_data)
    decrypted_data = decrypt_cipher.decrypt(decoded_encrypted_data)
    return StripPadding(decrypted_data, INTERRUPT, PAD)


our_data_to_encrypt = 'qwet'
encrypted_data = EncryptWithAES(cipher_for_encryption, our_data_to_encrypt)
print('Encrypted string:', encrypted_data)
print('Encrypted string:', encrypted_data.decode('utf8'))

# And let's decrypt our data
decrypted_data = DecryptWithAES(cipher_for_decryption, encrypted_data)
print('Decrypted string:', decrypted_data)
