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

password = input(f"Enter the password you want add to the Dictionary: {bcolors.HEADER}")
print(f"{bcolors.ENDC}")

# Open Default Wordlist for appending at the end of the file without truncating it. Creates a new file if it does not exist.
with open('Wordlists/Wordlist.txt', 'a') as f:
    print(password, file=f)
    print(f"{bcolors.OKGREEN}{password} added to the wordlist successfully!{bcolors.ENDC}")
    print()
