import hashlib
user_hash_dict = {}

# We gonna open all the passwords on read mode as a file that are located under the directory Passwords Lists
# I'm gonna add a wildcard so users can upload other passwords or dictionaries in .txt format 
with open ("PasswordsList.txt", "r") as f:
    passwords_list = f.read().splitlines()

with open("Username-HashedPasswords.txt", "r") as f:
    username_hashed_passwords = f.read().splitlines()
    for user_hash in username_hashed_passwords:
        # Here we are splitting the username from the hashes taking the : as entry point, using the 0 and 1 index to select the username and the hashed password
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash

for password in passwords_list:
    # Get the HASH for the Password List
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashed_password == hash:
            print(f'MGK SHOOTED AN USER, LOOTING HIS PASSWORD:\n\n{username}:{password}\n')
