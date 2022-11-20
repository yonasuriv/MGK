
![MGK](https://user-images.githubusercontent.com/59540565/202909145-17b11452-9393-46fb-9031-939a03ac7172.png)

# Assignment

![Disclaimer](https://user-images.githubusercontent.com/59540565/202909148-f8ace8b2-47c0-4eb8-97d1-0b3d0ab9e324.png)


1. Write your own basic version of the John The Ripper password cracking tool using Python.
2. Demonstrate it.
3. Talk us through your code and how you decided to approach the project. .
4. Your program should as a minimum be able to perform bruteforce and dictionary attacks, **everything else is left up to you to decide**.

## About
**MGK** was created to be a basic and light-weight version of **John the Ripper**.
 
It's written in **Python** as the main coding language,
and the GUI it's written using **Shell Scripting** *(BASH)*.
 
It's main functionalities are **Dictionary Attacks** and **Brute Forcing Attacks**.

### Default Settings

- By default it comes with the **SHA-256 HASH** for encrypted password as an encryption standard for most of the websites on the internet.
- By default it comes as a **PIN Cracker**, meaning it will only perform numbers attacks (0-9).

*The REASON for this is to prove the POTENTIAL of the script in matter of SECONDS.*

**ALL THE DEFAULT SETTINGS CHAN BE CHANGED** (*see how below*)

### Dependencies
`python3`

![QR-Updates](https://user-images.githubusercontent.com/59540565/202909147-18280669-b8f3-406e-9c46-f616403a2c62.png)

## Features
### Hash Generator
Although it is a feature of MGK, it runs separately.

To run it simply type on the console `python3 hashgen.py `

It lets you convert ANY password into SHA-256 HASH. 

You can also modify it to convert the password into another Secure Hash Algorithm.

Supported Types: **MD5**, **SHA1**, **SHA224**, **SHA256**, **SHA384**, and **SHA512**

To do it, simply open the HASHGEN.py file and modify the line 8, changing the sha256 for the one you like:

`hash = hashlib.sha256(password.encode("utf-8"))`

### Dictionary Attack
 
**MGK** comes with a dictionary of arround 900 potential passwords. 
 
 Theres is also an option to upgrade MGK with two sets of dictionaries that are located in the folder 'Password Atlas' as **torrent** files.
 
1. **Human-Only**: Contains over 64 MILLON *Real Human* passwords leaked from various website databases.
#### Size: 247 MB compressed. 684 MB uncompressed. 
2. **Arsenal-90**: Contains almost every wordlist, dictionary, and password database leaks, including every word in the Wikipedia databases (pages-articles, retrieved 2010, all languages) as well as lots of books from Project Gutenberg. It also includes the passwords from some low-profile database breaches that were being sold in the underground years ago.
#### Size: 4.2 GB compressed. 15 GB uncompressed. 

The format of the lists are in an standard text file sorted in non-case-sensitive alphabetical order. 


#### To update the Dictionary of MGK, simply add the passwords to the file `passwords_list.txt`

> **WARNING:** Opening a text file that's heavy it may cause your computer to freeze or even crash, to avoid that use the File Splitter (see below)

### File Spliter
Load your **MGK** with **Incendiary Bullets**, letting you split big texts files or dictionaries.

To do it simply head to *File Splitter* in *Password Atlas* and run `sh IncendiaryBullets.sh` in the terminal.

Your file to be splitted should be placed in the **Dictionary** folder.

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




