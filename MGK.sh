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
echo "  1) Run Dictionary Attack"
echo "  2) Add a Custom Password to the Dictionary"
echo "  3) Run Brute Force Attack (Default Mode: PIN Cracker)"
echo ""
echo "  4) Open MGK Manual (README.md on GitHub Repo, requires internet)"
echo "  0) Exit"
echo
echo -n "Choose one of the above options: "
}

main_menu  () {
read selection
echo
case $selection in
  1) python3 DictionaryAttack.py; credits;;
  2) python3 .addpwd.py ; credits;;
  3) python3 BruteForceAttack.py ; credits;;
  4) open https://github.com/yonasuriv/MGK;;
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
