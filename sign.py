#!/usr/local/env python

import sys
import base64
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def private_key_encrypt(message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_msg = cipher.encrypt(bytes(message, 'utf-8'))
    enc_text = base64.b64encode(encrypted_msg)
    return enc_text


def sign_license(email, expiry, private_key):
    message = f'{email}:{expiry}'
    return private_key_encrypt(message, private_key)


def read_public_key(filename):
    with open(filename, "rb") as f:
        return RSA.importKey(f.read())
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sign.py <private_key_file> <email> <expiry>")
        sys.exit(1)
    
    key = read_public_key(sys.argv[1])
    email = sys.argv[2]
    expiry, = sys.argv[3:4] or [ str(int(time.time())) ]
    
    print(sign_license(email, expiry, key))
