from Crypto.PublicKey import RSA

# generate public key
def generate_key_pair(bits = 1024):
    key = RSA.generate(bits)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def write_key_to_file(key, filename):
    with open(filename, "wb") as f:
        f.write(key.exportKey("PEM"))


# Main
if __name__ == "__main__":
    priv, pub = generate_key_pair()
    write_key_to_file(priv, "secrets/private.pem")
    write_key_to_file(pub, "secrets/public.pem")
