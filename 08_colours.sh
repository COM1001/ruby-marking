#!/bin/bash

REPO=$1
SCRIPT=$REPO/floodit.rb

if [ ! -e $REPO/Gemfile ]; then
  echo "[-] Gemfile does not exist, can't check for gem to colourise."
  exit 1
fi

if [ ! -e $REPO/Gemfile.lock ]; then
  echo "[-] Gemfile.lock does not exist, can't check for gem to colourise."
  exit 1
fi

cd $REPO

# TODO: Check if installed without bundler?

GEMS=$(grep -E "\bgem\b" Gemfile | grep -v console_splash | grep -vE "^#" | wc -l)

if [ $GEMS -ge 1 ]; then
    GEMS=$(bundle list | grep -v console_splash | grep -v bundler | wc -l)
    if [ $GEMS -lt 2 ]; then
	echo "[-] No additional gems found in Gemfile"
	exit 1
    fi
    GEMS=$(grep -E "\bgem\b" Gemfile | grep -v console_splash | grep -vE "^#" | awk '{print $2}' | tr '\n' ' ')

    echo "[+] Additional Gems used: $GEMS"
else
    echo "[-] Found no Gems besides console_splash."
    exit 1
fi
