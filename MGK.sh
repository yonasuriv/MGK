#!/bin/bash
. ./.assets/SHCSS.sh

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
echo "  1)$green2 Brute Force$end"
echo "  2)$green2 Dictionary Attack$end"
echo "  3) Dictionary File Splitter$end"
echo "  4) HASH Generator"
echo "  5) Add a custom password to the Passwords Directory"
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
  1) python3 .BruteForce.py;;
  2) python3 .DictionaryAttack.py;;
  3) sh .FileSplitter.sh;;
  4) python3 .HASHGEN.py;;
  5) python3 .ADDPWD.py ;;
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
clear
echo "$blink
█▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀   █▀▀ █░█ █▄░█   █▄▀ █▀▀ █░░ █░░ █▄█  
█░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄   █▄█ █▄█ █░▀█   █░█ ██▄ █▄▄ █▄▄ ░█░  

█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄▄ █▀▄ █▀█ █▄▄ █░█ ██▄ █▀▄

█▀▄ █▀▀ █░█ █▀▀ █░░ █▀█ █▀█ █▀▀ █▀▄   █▄▄ █▄█
█▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▄▀   █▄█ ░█░

░░█ █▀█ █▄░█ ▄▀█ ▀█▀ █░█ ▄▀█ █▄░█   █▀▄ █   █▀█ █ █▀▀ █▀█
█▄█ █▄█ █░▀█ █▀█ ░█░ █▀█ █▀█ █░▀█   █▄▀ █   █▀▄ █ █▄▄ █▄█

█▀▀ █▀█ █▀█
█▀░ █▄█ █▀▄

█░█░█ █ ▀█▀ █░█ █▀ █▀▀ █▀▀ █░█ █▀█ █▀▀
▀▄▀▄▀ █ ░█░ █▀█ ▄█ ██▄ █▄▄ █▄█ █▀▄ ██▄
$end"
}

# Script Start
clear
logo
menu
main_menu
