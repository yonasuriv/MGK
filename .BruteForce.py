# Using random module to generate random numbers
import random

# Using pyautogui to generate a more modern and interactive input box outside the console
import pyautogui

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

# Creating a menu option to let the user decide which type of characters want to use for the brute force
menu_options = {
    1: 'Digits                      [0123456789]',
    2: 'HEX Digits                  [0123456789abcdefABCDEF]',
    3: 'Lowercase letters           [abcdefghijklmnopqrstuvwxyz]',
    4: 'Uppercase letters           [ABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    5: 'All letters                 [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    6: 'All numbers and letters     [0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    7: 'All possible characters     [digits, letters, punctuation and whitespace]',   
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
            option = int(input('Select the bullets you want to use in the attack (1-7): '))
        except:
            print('Wrong input. Please enter a number between 1 and 7.')
        # Check what choice was entered and act accordingly
        if option == 1:
            chars = string.digits
            print()
            print(f'{bcolors.WARNING}You selected DIGITS Bullets ' + "(" +chars+ ")")
            break
        elif option == 2:
            chars = string.hexdigits
            print()
            print(f'{bcolors.WARNING}You selected HEXDIGITS Bullets ' + "(" +chars+ ")")
            break
        elif option == 3:
            chars = string.ascii_lowercase
            print()
            print(f'{bcolors.WARNING}You selected LOWERCASE Bullets ' + "(" +chars+ ")")
            break
        elif option == 4:
            chars = string.ascii_uppercase
            print()
            print(f'{bcolors.WARNING}You selected UPPERCASE Bullets ' + "(" +chars+ ")")
            break
        elif option == 5:
            chars = string.ascii_letters
            print()
            print(f'{bcolors.WARNING}You selected ABECEDARY Bullets ' + "(" +chars+ ")")
            break
        elif option == 6:
            chars = string.printable[:62]
            print()
            print(f'{bcolors.WARNING}You selected ARMOR-PIERCING Bullets ' + "(" +chars+ ")")
            break
        elif option == 7:
            chars = string.printable[:95]
            print()
            print(f'{bcolors.WARNING}You selected GODKILLER Bullets ' + "(" +chars+ ")")
            break
        else:
            chars = string.digits
            print()
            print(f'{bcolors.FAIL}Invalid option. {bcolors.WARNING}Running PIN CRACKER Default Mode (0123456789)')
            break

# Taking the character lists from the user selection
chars_list = list(chars)

print()
print(f'{bcolors.FAIL}WARNING: Selecting a Password OUTSIDE the Character Range will end in a Infinite Loop, shooting WITHOUT success.{bcolors.ENDC}')
# time.sleep(3)

# Password GUI
password = pyautogui.password("Enter a PIN/Password: ")

# Leaving the value equal to nothing since we dont want a fixed value, we want an output from the user
guess_password = ""

# Adding sleep time and text output to make the script look more modern
print()
print(f"{bcolors.OKGREEN}Preparing to launch the Bullets Rain..{bcolors.ENDC}")
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



