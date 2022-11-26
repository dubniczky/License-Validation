py := python
priv_file := "secrets/private.pem"
pub_file := "secrets/public.pem"
license_file := "licenses/1.pem"


# Generate a license
sign::
	$(py) sign.py $(priv_file) richard@example.com

# Verify a license
verify::
	$(py) verify.py $(pub_file) $(license_file) richard@example.com 1699746895017
