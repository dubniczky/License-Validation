#!/usr/local/env python

import sys
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


def sign_license(email, expiry, private_key):
    message = f'{email}:{expiry}'
    # hash
    digest = SHA256.new()
    digest.update(message.encode('utf-8'))
    # sign
    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(digest)
    return signature.hex()


def read_private_key(filename):
    with open(filename, "rb") as f:
        return RSA.importKey(f.read())
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sign.py <private_key_file> <email> <expiry?>")
        sys.exit(1)
    
    key = read_private_key(sys.argv[1])
    email = sys.argv[2]
    expiry, = sys.argv[4:5] or [ str(int((time.time() + 31_536_000) * 1000)) ] # default expiry: 1 year

    
    print(sign_license(email, expiry, key))
    print(email, expiry)
