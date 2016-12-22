#!/bin/bash

REPO=$1
GEM_HOME=/home/codio/.gems
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin"

RUBOCOP_FILE=/tmp/rubocop_tmp.yml
echo "Metrics/MethodLength:" > $RUBOCOP_FILE
echo "  Max: 30" >> $RUBOCOP_FILE

OUTPUT=$(rubocop -c $RUBOCOP_FILE --only MethodLength,GlobalVars -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Well modularised code"
    rm $RUBOCOP_FILE
    exit 0
else
    echo "[-] Not well modularised code. Here is the output of Rubocop:"
    rubocop -c $RUBOCOP_FILE --only MethodLength,GlobalVars -D $REPO/floodit.rb
    rm $RUBOCOP_FILE
    exit 1
fi


