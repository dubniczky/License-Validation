priv_file := "secrets/private.pem"
pub_file := "secrets/public.pem"
license_file := "secrets/license.txt"

# Generate a license
sign::
	python sign.py $(priv_file) richard@example.com

# Verify a license
verify::
	python verify.py $(pub_file) $(license)