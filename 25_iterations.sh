#!/bin/bash

REPO=$1

# Bad: for
if cat $REPO/floodit.rb | sed -e 's/"[^"].*"//g' | sed -e 's/#.*$//g'  | grep -Eq '\bfor\b'; then
    echo "[-] Use of standard for loops found"
    exit 1
fi

# Good: .each
if cat $REPO/floodit.rb | sed -e 's/"[^"].*"//g' | sed -e 's/#.*$//g' | grep -Eq '\.each\b'; then
    echo "[+] Found .each iteration"
    exit 0
fi

if cat $REPO/floodit.rb | sed -e 's/"[^"].*"//g' | sed -e 's/#.*$//g' | grep -Eq '\.each_with_index\b'; then
    echo "[+] Found .each_with_index iteration"
    exit 0
fi


echo "[-] Found no Ruby .each iterations"
exit 1
