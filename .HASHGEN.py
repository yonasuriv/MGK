# Importing HASH Libraries 
import hashlib

# Asking the user to type the password that want to be hashed
password = input("Enter the password you want to generate a HASH: \n\n")

# By default, strings in Python are Unicode, meaning you have to encode it into UTF-8
# Then it will print the password hashed using the method hashdigest, otherwise it will show you a hash object, and that's not what we want

# MD5 HASH
print()
hash = hashlib.md5(password.encode("utf-8"))
print("MD5:      " + hash.hexdigest())

# SHA1 HASH
print()
hash = hashlib.sha1(password.encode("utf-8"))
print("SHA1:     " + hash.hexdigest())

# SHA224 HASH
print()
hash = hashlib.sha224(password.encode("utf-8"))
print("SHA224:   " + hash.hexdigest())

# SHA256 HASH
print()
hash = hashlib.sha256(password.encode("utf-8"))
print("SHA256:   " + hash.hexdigest())

# SHA384 HASH
print()
hash = hashlib.sha384(password.encode("utf-8"))
print("SHA384:   " + hash.hexdigest())

# SHA512 HASH
print()
hash = hashlib.sha512(password.encode("utf-8"))
print("SHA512:   " + hash.hexdigest())

print()
