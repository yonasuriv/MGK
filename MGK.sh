#!/bin/bash
. ./.Assets/SHCSS.sh

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
echo "  1) Run$green2 Dictionary Attack$end"
echo "  2) Run$green2 Brute Force Attack$end $green(Default Mode: PIN Cracker)$end"
echo "  3) Run HASH Generator $green(Default Mode: SHA-256)$end"
echo "  4) Run Dictionary File Splitter $green(Incendiary Bullets Script)$end"
echo "  5) Add a Custom Password to the Passwords Directory"
echo ""
echo "  9) Open$white MGK Documentation Manual$end $green(Official GitHub Repository, requires internet)$end"
echo "  0) Exit"
echo
echo -n "Choose one of the above options: "
}

main_menu  () {
read selection
echo
case $selection in
  1) python3 .Dictionary.py; credits;;
  2) python3 .BruteForce.py ; credits;;
  3) python3 .HASHGEN.py;;
  4) sh .FileSplitter.sh;;
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
