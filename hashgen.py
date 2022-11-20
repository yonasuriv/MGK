# Import HASH Libraries 
import hashlib

password = input("Enter the password you want to generate a HASH: \n")
# Even that hashlib supports MD5, SHA1, SHA224, SHA256, SHA384, and SHA512, and to make the script faster, since is a beta version
# I'll be using  SHA256 as an standard rule for most of the encryptions on the internet
# By default, strings in Python are Unicode, meaning you have to encode it into UTF-8
hash = hashlib.sha256(password.encode("utf-8"))
# Print the password hashed using the method hashdigest, otherwise it will show you a hash object, and that's not what we want
print(hash.hexdigest())
