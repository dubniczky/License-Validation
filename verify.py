#!/usr/local/env python

import sys
import base64
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def public_key_decrypt(encrypted_msg, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.decrypt(base64.b64decode(encrypted_msg))


def read_public_key(filename):
    with open(filename, "rb") as f:
        return RSA.importKey(f.read())
    
    
def read_signature_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return f.read()
    
    
def verify_license(email, expiry, signature, public_key):
    message = f'{email}:{expiry}'
    print(message)
    return message == public_key_decrypt(signature, public_key).decode('utf-8')

def verify_expiry(expiry):
    return time.time() < float(expiry) / 1000.0

def verify(email, expiry, signature, public_key):
    return verify_expiry(expiry) and verify_license(email, expiry, signature, public_key)
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python verify.py <public_key_file> <signature_file> <email> <expiry?>")
        sys.exit(1)
    
    key = read_public_key(sys.argv[1])
    signature = read_signature_file(sys.argv[2])[0:-1]
    email = sys.argv[3]
    expiry, = sys.argv[4:5] or [ str(int((time.time() + 31_536_000) * 1000)) ] # default expiry: 1 year
    
    print(signature, email, expiry)
    
    print('valid' if verify(email, expiry, signature, key) else 'invalid')
