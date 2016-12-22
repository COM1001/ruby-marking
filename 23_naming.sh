#!/bin/bash

REPO=$1
GEM_HOME=/home/codio/.gems
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

OUTPUT=$(rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Naming according to style guide"
    exit 0
else
    echo "[-] Naming does not confirm to style guide. Here is the output of Rubocop:"
    rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb
    exit 1
fi

