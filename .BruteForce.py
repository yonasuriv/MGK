# We use random module to generate random numbers
import random

# We use pyautogui to generate a more modern and interactive input box outside the console
import pyautogui

# We use string module to get all the possible characters, altough we will be using only numbers (PIN Cracking) to make the Brute Force Faster
# Usefull for PIN Cracking# For string module documentation: https://docs.python.org/3/library/string.html
import string

# We import time module for the function sleep
import time

menu_options = {
    1: 'Digits (Default)            [0123456789]',
    2: 'HEX Digits                  [0123456789abcdefABCDEF]',
    3: 'Lowercase letters           [abcdefghijklmnopqrstuvwxyz]',
    4: 'Uppercase letters           [ABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    5: 'All letters                 [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    6: 'All numbers and letters     [0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]',
    7: 'All possible characters     [digits, letters, punctuation and whitespace]',   
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

print_menu()

if __name__=='__main__':
    while(True):
        try:
            print ()
            print(' Below you will be asked to select the type of characters that you want to include in the attack.')
            print(' Have in mind that selecting a password outside the character range will end in a infinite shooting without success.')
            print()
            option = int(input('Select your bullets (char type): '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            chars = string.digits
            print()
            print('You selected DIGITS Bullets ' + "(" +chars+ ")")
            break
        elif option == 2:
            chars = string.hexdigits
            print()
            print('You selected HEXDIGITS Bullets ' + "(" +chars+ ")")
            break
        elif option == 3:
            chars = string.ascii_lowercase
            print()
            print('You selected LOWERCASE Bullets ' + "(" +chars+ ")")
            break
        elif option == 4:
            chars = string.ascii_uppercase
            print()
            print('You selected UPPERCASE Bullets ' + "(" +chars+ ")")
            break
        elif option == 5:
            chars = string.ascii_letters
            print()
            print('You selected ABECEDARY Bullets ' + "(" +chars+ ")")
            break
        elif option == 6:
            chars = string.printable[:62]
            print()
            print('You selected ARMOR-PIERCING Bullets ' + "(" +chars+ ")")
            break
        elif option == 7:
            chars = string.printable[:95]
            print()
            print('You selected GODKILLER Bullets ' + "(" +chars+ ")")
            break
        else:
            chars = string.digits
            print('Invalid option. Running Default Mode (PIN Cracker).')
            break

chars_list = list(chars)

password = pyautogui.password("Enter a PIN/Password: ")
guess_password = ""
print()
print("Preparing to launch the bullets rain..")
time.sleep(3)

while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print("︻╦̵̵͇̿̿̿̿╤──"+ "   " + str(guess_password))

	if(guess_password == list(password)):
		print("Your PIN/Password is: " + "".join(guess_password))
		break
		exit



