#!/bin/bash
. ./.assets/SHCSS.sh

echo "You are about to load MGK with Incendiary Bullets (Dictionary File Splitter)."
sleep 3
echo
echo " Please have in mind a few things:"
echo ""
echo " 1) $green2 Your passwords file should be under the directory 'Passwords Atlas'. $end"
echo " 1) $green2 When writting the file name, it should be EXACT.. $end"
echo " 2) $green2 You don't have to write the extension, as for the moment the script ONLY suport .TXT files. $end"
echo
sleep 3
echo " If the file get splitted succesfully, you should see something similar to this:$green xaa$end,$green xab$end,$green xac$end,$green xad$end,$green xae$end...$green xagsr$end,$green xagso$end,$green xagsp$end,$green xagsq$end, etc."
echo 
echo "$yellow2 Enter the name of the file you want split: $end"
echo
read fileName
echo
echo "$yellow Enter the maximum number of lines that your file can have (recommended: 5000): $end"
echo
read fileLines
echo

cd 'Wordlists'
split $fileName.txt -l $fileLines
