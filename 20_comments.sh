#!/bin/bash

REPO=$1

COMMENTS=$(grep -E ".*#[^\{].*$" $REPO/floodit.rb | sed -e 's/^.*#//g')

if [ $(echo $COMMENTS | wc -l) -lt 10 ]; then
    echo "[+] Well documented code"
    exit 0
else
    echo "[-] Not well documented code"
    exit 1
fi

