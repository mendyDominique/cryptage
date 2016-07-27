# -*-coding:utf-8 -*-
from Crypto.Cipher import AES
import base64


def teste(mess):
    message = mess
    obj = AES.new('0123456789123456', AES.MODE_CFB, 'This is an IV456')
    return base64.b64encode(obj.encrypt(message))




pret = teste('je vais a lécole')
print(pret)
print("------------------------------------------------------------------")

def decode(mess):
    ciphertext = mess
    obj2 = AES.new('0123456789123456', AES.MODE_CFB, 'This is an IV456')
    return obj2.decrypt(base64.b64decode(ciphertext))



taxe = decode('')
print(taxe)