#!/bin/bash
. ./.shcss.sh

logo () {
echo """

█████████████████████████████████████████████████▀████████████████████████████████████████████████
█▄─▀█▀─▄██▀▄─██─▄▄▄─█─█─█▄─▄█▄─▀█▄─▄█▄─▄▄─███─▄▄▄▄█▄─██─▄█▄─▀█▄─▄███▄─█─▄█▄─▄▄─█▄─▄███▄─▄███▄─█─▄█
██─█▄█─███─▀─██─███▀█─▄─██─███─█▄▀─███─▄█▀███─██▄─██─██─███─█▄▀─█████─▄▀███─▄█▀██─██▀██─██▀██▄─▄██
▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
"""
}

menu () {
echo "$negative MENU $end"
echo
echo "  1)$red Run Dictionary Attack$end"
echo "  2)$red Run Brute Force Attack (Default Mode: PIN Cracker)$end"
echo "  3)$yellow2 Run HASH Generator (Default Mode: SHA-256)$end"
echo "  4)$yellow2 Run Incendiary Bullet File Splitter$end"
echo "  5)$yellow2 Add a Custom Password to the Passwords Directory$end"
echo ""
echo "  9)$white Open MGK Documentation and Manual (Official GitHub Repository, Requires Internet)$end"
echo "  0) Exit"
echo
echo -n "Choose one of the above options: "
}

main_menu  () {
read selection
echo
case $selection in
  1) python3 DictionaryAttack.py; credits;;
  2) python3 BruteForceAttack.py ; credits;;
  3) python3 hashgen.py;;
  4) cd 'Password Atlas' && cd 'File Spliter' && sh IncendiaryBullets.sh;;
  5) python3 .addpwd.py ; credits;;
  9) open https://github.com/yonasuriv/MGK;;
  0) credits;;
  *) incorrect_selection_number;;
esac
}

incorrect_selection_number() {
  echo -n "$red  Incorrect selection, try again: $end"
  main_menu
  echo
}

credits () {
echo "$blink
█▀▄▀█ █▀▀ █▄▀   █▀▄ █▀▀ █░█ █▀▀ █░░ █▀█ █▀█ █▀▀ █▀▄   █▀▀ █▀█ █▀█   █░█░█ █ ▀█▀ █░█ █▀ █▀▀ █▀▀ █░█ █▀█ █▀▀
█░▀░█ █▄█ █░█   █▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▄▀   █▀░ █▄█ █▀▄   ▀▄▀▄▀ █ ░█░ █▀█ ▄█ ██▄ █▄▄ █▄█ █▀▄ ██▄
$end"
}

# Script Start
clear
logo
menu
main_menu
