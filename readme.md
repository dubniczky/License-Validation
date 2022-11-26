# License Validation

A public key-based offline license validation protocol

## Description

In some software, license validation is not practical with the use of online services. This is an offline implementation of license validation using asymmetric digital signature in python.

The user name and the expiration date are joined and encrypted with the private key, which could happen on a server once during purchase. Then the signature is sent to the user and entered into the application. The application has the public key pair of the server pre-packaged and will use it to check the validity of the signature and the expiration date.

## Usage

Create key pair

```bash
make generate
```

Create test signature

```bash
make sign
```

Validate test signature

```bash
make verify
```