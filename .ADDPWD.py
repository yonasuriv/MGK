password = input("Enter the password you want add to the Dictionary: \n")

with open('Passwords-List.txt', 'a') as f:
    print(password, file=f)
