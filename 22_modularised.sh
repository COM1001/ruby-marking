#!/bin/bash

REPO=$1

RUBOCOP_FILE=/tmp/rubocop_tmp.yml
echo "Metrics/MethodLength:" > $RUBOCOP_FILE
echo "  Max: 20" >> $RUBOCOP_FILE

OUTPUT=$(rubocop -c $RUBOCOP_FILE --only MethodLength -D $REPO/floodit.rb)

rm $RUBOCOP_FILE

if [ $? -eq 0 ]; then
    echo "[+] Well modularised code"
    exit 0
else
    echo "[-] Not well modularised code:"
    echo $OUTPUT
    exit 1
fi

