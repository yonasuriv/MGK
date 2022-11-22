# Using random module to generate random numbers
import random

# Using pyautogui to generate a more modern and interactive input box outside the console
# import pyautogui

# Using string module to get all the possible characters
# For string module documentation: https://docs.python.org/3/library/string.html
import string

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

# Password GUI Prompt
# password = pyautogui.password("Enter a PIN/Password: ")

# Password Promt
password = input(f"Enter a PIN/Password to perform the Brute Force: {bcolors.HEADER}")
print(f"{bcolors.ENDC}")

#def char_warning():
#    print()
#    print(f'{bcolors.FAIL}WARNING: Selecting a Password OUTSIDE the Character Range will end in a Infinite Loop, shooting WITHOUT success.{bcolors.ENDC}')
#    # time.sleep(3)
#    }
#
#char_warning()
    
# Creating a menu option to let the user decide which type of characters want to use for the Brute Force
menu_options = {
    1: f'{bcolors.UNDERLINE}Digits{bcolors.ENDC}                      {bcolors.OKGREEN}[0123456789]{bcolors.ENDC}',
    2: f'{bcolors.UNDERLINE}HEX Digits{bcolors.ENDC}                  {bcolors.OKGREEN}[0123456789abcdefABCDEF]{bcolors.ENDC}',
    3: f'{bcolors.UNDERLINE}Lowercase letters{bcolors.ENDC}           {bcolors.OKGREEN}[abcdefghijklmnopqrstuvwxyz]{bcolors.ENDC}',
    4: f'{bcolors.UNDERLINE}Uppercase letters{bcolors.ENDC}           {bcolors.OKGREEN}[ABCDEFGHIJKLMNOPQRSTUVWXYZ]{bcolors.ENDC}',
    5: f'{bcolors.UNDERLINE}All letters{bcolors.ENDC}                 {bcolors.OKGREEN}[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]{bcolors.ENDC} ',
    6: f'{bcolors.UNDERLINE}All numbers and letters{bcolors.ENDC}     {bcolors.OKGREEN}[0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]{bcolors.ENDC}',
    7: f'{bcolors.UNDERLINE}All possible characters{bcolors.ENDC}     {bcolors.OKGREEN}[digits, letters, punctuation and whitespace]{bcolors.ENDC}',   
}

# Making the menu interactive
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
# Print the menu
print_menu()

# Adding the values to each of the options on the menu
if __name__=='__main__':
    while(True):
        try:
            print()
            option = int(input('Enter the type of bullets (characters) you to use in the attack (1-7): '))
        except:
            print('Wrong input. Please enter a number between 1 and 7.')
        # Check what choice was entered and act accordingly
        if option == 1:
            chars = string.digits
            print()
            print(f'You have selected {bcolors.HEADER}DIGITS{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 2:
            chars = string.hexdigits
            print()
            print(f'You have selected {bcolors.HEADER}HEXDIGITS{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 3:
            chars = string.ascii_lowercase
            print()
            print(f'You have selected {bcolors.HEADER}LOWERCASE{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 4:
            chars = string.ascii_uppercase
            print()
            print(f'You have selected {bcolors.HEADER}UPPERCASE{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 5:
            chars = string.ascii_letters
            print()
            print(f'You have selected {bcolors.HEADER}ABECEDARY{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 6:
            chars = string.printable[:62]
            print()
            print(f'You have selected {bcolors.HEADER}ARMOR-PIERCING{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        elif option == 7:
            chars = string.printable[:95]
            print()
            print(f'You have selected {bcolors.HEADER}GODKILLER{bcolors.ENDC} Bullets ' + f"{bcolors.HEADER}(" +chars+ ")")
            break
        else:
            print()
            print(f'{bcolors.FAIL}Invalid option. Try again.{bcolors.ENDC}')
            break

# Taking the character lists from the user selection
chars_list = list(chars)

# Leaving the value equal to nothing since we dont want a fixed value, we want an output from the user
guess_password = ""

# Output all the possible combinations of characters lenght + characters type
print(f"{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}The total amount of characters for the PIN/Password you've entered is: {bcolors.OKCYAN}" + str(len(password)))
print(f"{bcolors.OKBLUE}The total amount of characters that will be used on the attack is: {bcolors.OKCYAN}" + str(len(chars)))
print(f"{bcolors.OKBLUE}The total amount of all the possible combinations (lenght and complexity) is: {bcolors.OKCYAN}" + str(len(password)**len(chars)))
print(f"{bcolors.ENDC}")
time.sleep(3)

# Adding a PRESS ENTER to continue so the user can read the output above
input("Press any key to launch the attack...")

# Adding sleep time and text output to make the script look more modern
print()
print(f"{bcolors.WARNING}Preparing to launch the Bullets Rain..{bcolors.ENDC}")
print()
time.sleep(3)

# If password is not equal to the one entered, it will keep performing the brute force attack showing the random characters used
while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print("︻╦̵̵͇̿̿̿̿╤──  "+ "   " + str(guess_password))
	print()

# If the password is equal to the one entered, it will show the final output (result)
	if(guess_password == list(password)):
		print("🆃🅷🅴 🅵🅾🆁🅲🅴🅳 🅿🅰🆂🆂🆆🅾🆁🅳 🆆🅰🆂 " + "".join(guess_password))
		print()
		break
		exit


