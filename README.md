
![MGK](https://user-images.githubusercontent.com/59540565/202909145-17b11452-9393-46fb-9031-939a03ac7172.png)
# TABLE OF CONTENTS
1. [About](#about)
2. [Approach](#approach)
4. [Launch the Script & Dependencies](#start)
5. [Features & Tools](#features)
6. [Configuration & Default Settings](#configuration)
7. [Updates](#QR-Updates)

----

![Disclaimer](https://user-images.githubusercontent.com/59540565/202909148-f8ace8b2-47c0-4eb8-97d1-0b3d0ab9e324.png)

## ABOUT
**Machine Gun Kelly** is a free password cracking software tool in Alpha.
It was created to be a basic and light-weight version of **John the Ripper**.

**Did you know?**
John the Ripper was a serial killer, MGK was a rapper, I mean, a robber and a kidnaper.
 
It's written in **Python** as the main coding language,
and the GUI it's written using **Shell Scripting** *(BASH)*.
 
It's main functionalities are **Dictionary Attacks** and **Brute Forcing**.

### Approach

 1. Created the Script on **Python**: HASH Generator.
 2. Created the Script on **Python**: Bruce Force.
 3. Created the Script on **Python**: Dictionary Attack.
 4. Created the Script on **Python**: to permanently add custom passwords to the Password List.
	 *(for Dictionary Attack)*
 6. Created the Script on **BASH**: Dictionary File Splitter 
	*This was created after playing with the Dictionary Attack, and after seeing it working, I downloaded some really-heavy dictionaries but when I tried to open it my computer froze, so this will avoid that at all costs.*
 7. Connect all the scripts using **BASH** for the interface.
	 *Simply to be more creative and for more fun.*
 8. Added *ASCII Art* and *Colors* to make the Script more User Friendly.



## START
To start MGK, open the terminal and write `sh MGK.sh`

### DEPENDENCIES
The following dependencies are required to run the script:

 - `python3`
 

## FEATURES

1. [Brute Force](#brute-force)
2. [Dictionary Attack](#dictionary-attack)
3. [Dictionary File Splitter](#third-example)
4. [HASH Generator](#hash-generator)

---

### BRUTE FORCE

**MGK** is by default coded to be a **PIN Cracker**, meaning that it will perform ONLY number attacks.

The reason of this is to see the results in the fastest time possible, trying the combination of all ten numbers (**0-9**)

---
    
### DICTIONARY ATTACK
 
**MGK** comes with a dictionary of arround 900 potential passwords. 
 
 Theres is also an option to upgrade MGK with two sets of dictionaries.
 These are located in the folder '**Passwords Atlas/Dictionary Downloads/**' as **torrent** files.
 
1. **Human-Killer**: Contains over 64 MILLON *Real Human Only* passwords leaked from various website databases.
#### Size: 247 MB compressed. 684 MB uncompressed. 
2. **Bio-Weapon**: Contains almost every wordlist, dictionary, and password database leaks, including every word in the Wikipedia databases (pages-articles, retrieved 2010, all languages) as well as lots of books from Project Gutenberg. It also includes the passwords from some low-profile database breaches that were being sold in the underground years ago.
#### Size: 4.2 GB compressed. 15 GB uncompressed. 

The format of the lists are in an standard text file sorted in non-case-sensitive alphabetical order. 


#### To update the Dictionary of MGK, simply add the passwords to the file `PasswordsList.txt`

> **WARNING:** 
> Opening a text file that's heavy it may cause your computer to freeze or even crash.
>To avoid that, use the Dictionary File Splitter. (see below)

---

### DICTIONARY FILE SPLITTER
Load your **MGK** with **Incendiary Bullets**, letting you split big texts files or dictionaries.

Your file to be splitted should be placed in the **PasswordsAtlas** folder.

The **recommended** maximum lines for a TXT file is **5000 lines**.

 - That means that the file would never exceed **100KB** 
 - Supports GitHub   Uploads

*Currently supports **ONLY TXT** Files.*

---

### HASH GENERATOR
It lets you convert ANY password into SHA-256 HASH by default. 

You can also modify it to convert the password into another Secure Hash Algorithm.

Supported Types: **MD5**, **SHA1**, **SHA224**, **SHA256**, **SHA384**, and **SHA512**

See [HASH Generator Configuration](#hash-generator-configuration)

## CONFIGURATION
### DEFAULT SETTINGS

- By default it comes with the **SHA-256 HASH** for encrypted password as an encryption standard for most of the websites on the internet.
- By default it comes as a **PIN Cracker**, meaning it will only perform numbers attacks (0-9).

*The REASON for this is to prove the POTENTIAL of the script in matter of SECONDS.*

**ALL THE DEFAULT SETTINGS CHAN BE CHANGED** (see below)

----

### CHANGE SETTINGS
To change the configuration of the MGK:

 1. Head to the directory **MGK** -> **View** -> **Show Hidden Files**. (or *CTRL+H*)

#### HASH GENERATOR CONFIGURATION
To do it, simply open the `.HASHGEN.py` file and modify the line 8, changing the sha256 for the one you like:

`hash = hashlib.sha256(password.encode("utf-8"))`

----


![QR-Updates](https://user-images.githubusercontent.com/59540565/202909147-18280669-b8f3-406e-9c46-f616403a2c62.png)


