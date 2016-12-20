#!/bin/bash

REPO=$1

# Bad: for
if grep -Eq '\bfor\b' $REPO/floodit.rb; then
    echo "[-] Use of standard for loops found"
    exit 1
fi

# Good: .each
if grep -Eq '\.each\b' $REPO/floodit.rb; then
    echo "[+] Found .each iteration"
    exit 0
fi

echo "[-] Found no Ruby .each iterations"
exit 1
