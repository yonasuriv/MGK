#  Machine Gun Kelly Password Cracker Manual

> QR Code to the GitHub Repository of MGK
![qr](https://user-images.githubusercontent.com/59540565/202887058-71f016eb-f217-4270-9871-2f336ae2543c.png)

## Assignment
1. Write your own basic version of the John The Ripper password cracking tool using Python,.
2. Demonstrate it.
3. Talk us through your code and how you decided to approach the project. .
4. Your program should as a minimum be able to perform bruteforce and dictionary attacks, **everything else is left up to you to decide**.

## About
**MGK** is a ripoff version of **John the Ripper**.

It's written in **Python** as the main coding language embedded with **Shell Scripting (BASH)** for a better looking interface..

It's a simple and light-weight version made in just 5 days as a test for [**WithSecure**](https://www.withsecure.com "WithSecure") Company.

**This is for educational purposes only and SHOULD NEVER be used in an Illegal Context.**

![VirtualBox_Parrot_20_11_2022_06_08_49](https://user-images.githubusercontent.com/59540565/202886668-aef8ef09-14f6-4f5c-b4d4-1418b7c24f13.png)

## Dependencies
`python3`

## Features
### Hash Generator
Although it is a feature of MGK, it runs separately.

To run it simply type on the console `python3 hashgen.py `

It lets you convert ANY password into SHA-256 Hash. 

You can also modify it to convert the password into another secure hash algorithms.

Supported Types: **MD5**, **SHA1**, **SHA224**, **SHA256**, **SHA384**, and **SHA512**

To do it, simply open the HASHGEN.py file and modify the line 8, changing the sha256 for the one you like:

`hash = hashlib.sha256(password.encode("utf-8"))`

### Dictionary Attack
 
**MGK** comes with a dictionary of arround 900 potential passwords. 
 
 Theres is also an option to upgrade MGK with two sets of dictionaries that are located in the folder 'Password Atlas' as torrent files.
 
1. **Human Only:** Contains over 64 MILLON *Real Human* passwords leaked from various website databases.
#### Size: 247 MB compressed. 684 MB uncompressed. 
2. **Final**: Contains almost every wordlist, dictionary, and password database leaks, including every word in the Wikipedia databases (pages-articles, retrieved 2010, all languages) as well as lots of books from Project Gutenberg. It also includes the passwords from some low-profile database breaches that were being sold in the underground years ago.
#### Size: 4.2 GB compressed. 15 GB uncompressed. 

The format of the lists are in an standard text file sorted in non-case-sensitive alphabetical order. 


#### To update the Dictionary of MGK, simply add the passwords to the file `passwords_list.txt`

### Brute Force Attack

**MGK** is by default coded to be a **PIN Cracker**, meaning that it will perform ONLY number attacks.

The reason of this is to see the results in the fastest time possible, trying the combination of all ten numbers (**0-9**)

You can also modify it to be get the full character list:

**0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~**

To do so, simply open the file BruteForceAttack.py and modify the value assigned to the variable char on the line 11:

`chars = string.printable[:10]`

#### Manual way: 
Update the value from 1 to 95.

#### Automated way:


##### string.ascii_lowercase

    The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. 

##### string.ascii_uppercase

    The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 

##### string.ascii_letters

    The concatenation of the ascii_lowercase and ascii_uppercase constants described above. 

##### string.digits

    The string '0123456789'.

##### string.hexdigits

    The string '0123456789abcdefABCDEF'.

##### string.octdigits

    The string '01234567'.

##### string.punctuation

    String of ASCII characters which are considered punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

##### string.whitespace

    String containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

##### string.printable

    String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.




