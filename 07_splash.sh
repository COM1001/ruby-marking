#!/bin/bash

REPO=$1
SCRIPT=$REPO/floodit.rb
GEM_HOME=/home/codio/.gems
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin"


function ensure_splash {
    gem install console_splash > /dev/null 2>&1
}

if [ ! -e $REPO/Gemfile ]; then
    echo "[-] Gemfile does not exist, can't check for splash gem."
    ensure_splash
    exit 1
fi

if [ ! -e $REPO/Gemfile.lock ]; then
    echo "[-] Gemfile.lock does not exist, can't check for splash gem."
    ensure_splash
    exit 1
fi

cd $REPO

bundle list | grep -q console_splash

if [ $? -ne 0 ]; then
    echo "[-] Gem console_splash is not bundled"
    ensure_splash
    exit 1					      
fi

workfile="/tmp/floodit_tmp.rb"

echo "require 'mocha/api'" > $workfile
echo "require 'console_splash'" >> $workfile
echo "ConsoleSplash.expects(:splash).returns(exit(27))" >> $workfile
cat floodit.rb >> $workfile

export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems
ruby $workfile

if [ $? -eq 27 ]; then
    echo "[+] Gem console_splash is used"
else
    echo "[-] Gem console_splash is installed but not used"
    exit 1
fi
