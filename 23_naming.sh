#!/bin/bash

REPO=$1
export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems:/home/codio/.gem/ruby/2.2.0:/var/lib/gems/2.2.0:/usr/share/rubygems-integration/2.2.0:/usr/share/rubygems-integration/all
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

gem install rubocop --conservative > /dev/null 2>&1

OUTPUT=$(rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Naming according to style guide"
    exit 0
else
    echo "[-] Naming does not conform to style guide. Check the output of Rubocop in /home/codio/workspace/autograding_logs/23_naming.log"
    rubocop --only ConstantName,VariableName,MethodName -D $REPO/floodit.rb > /home/codio/workspace/autograding_logs/23_naming.log
    exit 1
fi

