# We use random module to generate random numbers
import random

# We use pyautogui to generate a more modern and interactive input box outside the console
import pyautogui

# We use string module to get all the possible characters, altough we will be using only numbers (PIN Cracking) to make the Brute Force Faster
# Usefull for PIN Cracking# For string module documentation: https://docs.python.org/3/library/string.html
import string

chars = string.printable[:10] # :95 for the full characters list
chars_list = list(chars)

password = pyautogui.password("Enter a PIN/Password: ")
guess_password = ""

while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print("<==========="+ str(guess_password) + "===========>")

	if(guess_password == list(password)):
		print("Your PIN/Password is: " + "".join(guess_password))
		break
		exit

