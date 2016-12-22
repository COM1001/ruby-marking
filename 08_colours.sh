#!/bin/bash

REPO=$1
SCRIPT=$REPO/floodit.rb
export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems:/home/codio/.gem/ruby/2.2.0:/var/lib/gems/2.2.0:/usr/share/rubygems-integration/2.2.0:/usr/share/rubygems-integration/all
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

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
