#!/usr/local/env python

import sys
import time
import base64
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
    return signature


def read_private_key(filename):
    with open(filename, "rb") as f:
        return RSA.importKey(f.read())
    
def to_pem(license, email, expiry):
    metadata = f'{email}:{expiry}'.encode('utf-8')
    #return '\n'.join([
    #    '----- BEGIN APP LICENSE -----',
    #    base64.b64encode(license + metadata).decode('utf-8'),
    #    '----- END APP LICENSE -----',
    #])
    return base64.b64encode(license + metadata).decode('utf-8')
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sign.py <private_key_file> <email> <expiry?>")
        sys.exit(1)
    
    key = read_private_key(sys.argv[1])
    email = sys.argv[2]
    expiry, = sys.argv[4:5] or [ str(int((time.time() + 31_536_000) * 1000)) ] # default expiry: 1 year

    license = sign_license(email, expiry, key)
    print(to_pem(license, email, expiry))
