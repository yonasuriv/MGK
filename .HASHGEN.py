# Importing HASH Libraries 
import hashlib

# Adding colors to the terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Asking the user to type the password that want to be hashed
password = input(f"Enter the password you want to generate a HASH: {bcolors.OKGREEN}")


# By default, strings in Python are Unicode, meaning you have to encode it into UTF-8
# Then it will print the password hashed using the method hashdigest, otherwise it will show you a hash object, and that's not what we want

# MD5 HASH
print(f"{bcolors.ENDC}")
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
