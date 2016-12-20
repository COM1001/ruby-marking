#!/bin/bash

REPO=$1
SCRIPT=$REPO/floodit.rb

if [ ! -e $REPO/Gemfile ]; then
    echo "[-] Gemfile does not exist, can't check for splash gem."
    exit 1
fi

if [ ! -e $REPO/Gemfile.lock ]; then
    echo "[-] Gemfile.lock does not exist, can't check for splash gem."
    exit 1
fi

cd $REPO

bundle list | grep -q console_splash

if [ $? -ne 0 ]; then
  echo "[-] Gem console_splash is not bundled"
  exit 1					      
fi

workfile="/tmp/floodit_tmp.rb"

echo "require 'mocha/api'" > $workfile
echo "require 'console_splash'" >> $workfile
echo "ConsoleSplash.expects(:splash).returns(exit(27))" >> $workfile
cat floodit.rb >> $workfile

ruby $workfile

if [ $? -eq 27 ]; then
    echo "[+] Gem console_splash is used"
else
    echo "[-] Gem console_splash is installed but not used"
    exit 1
fi
