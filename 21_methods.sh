#!/bin/bash

REPO=$1

NUM_METHODS=$(grep -E "\bdef\b" $REPO/*.rb | wc -l)

if [ $NUM_METHODS -lt 3 ]; then
    echo "[-] Less than 3 methods"
    exit 1
else
    echo "[+] Basic use of methods"
    exit 0
fi


