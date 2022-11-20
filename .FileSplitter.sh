#!/bin/bash
. ./.Assets/SHCSS.sh

echo "You are about to load MGK with Incendiary Bullets (Dictionary File Splitter)."
sleep 3
echo
echo " Please have in mind a few things:"
echo ""
echo " 1) $red Your Passwords TXT File should be under the directory DICTIONARY. $end"
echo " 1) $red FILE NAME should be EXACT. $end"
echo " 2) $red You don't have to write the extension, as for the moment the script ONLY suport .TXT files. $end"
echo
sleep 3
echo " If the file get splitted succesfully, you should see something similar to this:$white xaa$end,$white xab$end,$white xac$end,$white xad$end,$white xae$end...$white xagsr$end,$white xagso$end,$white xagsp$end,$white xagsq$end, etc."
echo 
echo "$yellow Enter the name of the file you want split: $end"
echo
read fileName
echo
echo "$yellow Enter the maximum number of lines that your file should have: $end"
echo
read fileLines
echo

cd Dictionary
split $fileName.txt -l $fileLines
