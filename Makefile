py := python
priv_file := "secrets/private.pem"
pub_file := "secrets/public.pem"
license_file := "licenses/1.pem"


# Generate a license
sign::
	$(py) sign.py $(priv_file) richard@example.com 16997468950917 | tee $(license_file)

# Verify a license
verify::
	$(py) verify.py $(pub_file) $(license_file) richard@example.com 16997468950917

# Generate the key pair
generate::
	$(py) generate.py
