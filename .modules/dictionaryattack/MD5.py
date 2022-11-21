# Importing hashlib for the secure hashes and messages digests
import hashlib

# Importing time module for the function sleep
import time

user_hash_dict = {}

# Opens the passwords file on read mode as a file 
with open ("Wordlist.txt", "r") as f:
    passwords_list = f.read().splitlines()

# Opens the Username and Hashed Passwords file on read mode as a file 
with open("Username-Hashed-Passwords.txt", "r") as f:
    username_hashed_passwords = f.read().splitlines()
    for user_hash in username_hashed_passwords:
        # Splitting the username from the hashes taking the : as entry point, using the 0 and 1 index to select the username and the hashed password
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash

for password in passwords_list:
    # Get the HASH for the Password List
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashed_password == hash:
            print(f'︻╦̵̵͇̿̿̿̿╤── MGK SHOOTED AN USER, LOOTING HIS PASSWORD:\n\n{bcolors.FAIL}{username}:{password}{bcolors.ENDC}\n') # Using the bcloros from the DictionaryAttack.py 
