#!/bin/bash

REPO=$1

OUTPUT=$(rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Naming according to style guide"
    exit 0
else
    echo "[-] Naming does not confirm to style guide. Here is the output of Rubocop:"
    rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb
    exit 1
fi

