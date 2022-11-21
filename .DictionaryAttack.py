# Using time module for the function sleep
import time

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

# Adding sleep time and text output to make the script look more modern
print("Preparing the DE-HASHER Weapon Attachment...")
time.sleep(4)
print()

# Executes all the modules for all the secure hashes to check for all the passwords stored in wordlists with all the hashes below
# Print an input everytime it changes module
print(f"{bcolors.OKGREEN}Loading MD5 Bullets{bcolors.ENDC}")
print()
time.sleep(1)
exec(open("./.modules/dictionaryattack/MD5.py").read())

print(f"{bcolors.OKGREEN}Loading SHA1 Bullets{bcolors.ENDC}")
print()
time.sleep(1)
exec(open("./.modules/dictionaryattack/SHA1.py").read())

print(f"{bcolors.OKGREEN}Loading SHA224 Bullets{bcolors.ENDC}")
print()
time.sleep(1)
exec(open("./.modules/dictionaryattack/SHA224.py").read())

print(f"{bcolors.OKGREEN}Loading SHA256 Bullets{bcolors.ENDC}")
print()
time.sleep(2)
exec(open("./.modules/dictionaryattack/SHA256.py").read())

print(f"{bcolors.OKGREEN}Loading SHA384 Bullets{bcolors.ENDC}")
print()
time.sleep(2)
exec(open("./.modules/dictionaryattack/SHA384.py").read())

print(f"{bcolors.OKGREEN}Loading SHA512 Bullets{bcolors.ENDC}")
print()
time.sleep(2)
exec(open("./.modules/dictionaryattack/SHA512.py").read())

print("🅲🅰🆁🅽🅰🅶🅴 🅴🅽🅳🅴🅳")
print()

