#!/usr/local/env python

import re
import sys
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


def verify_license(email, expiry, license, public_key):
    message = f'{email}:{expiry}'
    # hash
    digest = SHA256.new()
    digest.update(message.encode('utf-8'))
    # verify
    verifier = PKCS1_v1_5.new(public_key)
    return verifier.verify(digest, bytes.fromhex(license))


def read_public_key(filename):
    with open(filename, "rb") as f:
        return RSA.importKey(f.read())
    
    
def read_signature_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return f.read()
    
    
def from_pem(pem):
    m = re.search('----- BEGIN APP LICENSE -----\n[a-zA-Z0-9/+=]+\n----- END APP LICENSE -----', pem, flags=re.M)
    if m:
        found = m.group(1)
        
    print(found)
    

def verify_expiry(expiry):
    return time.time() < float(expiry) / 1000.0

def verify(email, expiry, signature, public_key):
    return verify_expiry(expiry) and verify_license(email, expiry, signature, public_key)


    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python verify.py <public_key_file> <signature_file> <email> <expiry>")
        sys.exit(1)
    
    key = read_public_key(sys.argv[1])
    signature = read_signature_file(sys.argv[2])[0:-1]
    email = sys.argv[3]
    expiry = sys.argv[4]
    
    print(signature, email, expiry)
    
    print('valid' if verify(email, expiry, signature, key) else 'invalid')
