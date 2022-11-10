#!/usr/local/env python

import sys
from Crypto.PublicKey import RSA

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify.py <public_key_file>")
        sys.exit(1)
    with open(sys.argv[1], "rb") as f:
        key = RSA.importKey(f.read())
        print(key)