#!/bin/bash

REPO=/home/codio/workspace/flood-it
SCRIPT=$REPO/floodit.rb

if [ ! -d $REPO/Gemfile ]; then
  echo "[-] Gemfile does not exist, can't check for splash gem."
  exit 1
fi

if [ ! -d $REPO/Gemfile.lock ]; then
  echo "[-] Gemfile.lock does not exist, can't check for splash gem."
  exit 1
fi

cd $REPO

# TODO: Check if installed without bundler?

if $(bundle list | grep -q console_splash)); then
    echo "[-] Gem console_splash is not bundled"
fi
					   
echo "[+] Gem console_splash is installed with bundler.

# TODO: Mock splash.splash and check it is called (before hitting enter)

