#!/bin/bash

REPO=/home/codio/workspace/flood-it


OUTPUT=$(rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Naming according to style guide"
    exit 0
else
    echo "[-] Naming does not confirm to style guide:"
    echo $OUTPUT
    exit 1
fi

