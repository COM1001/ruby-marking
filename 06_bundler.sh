#!/bin/bash

REPO=/home/codio/workspace/flood-it

if [ ! -d $REPO/Gemfile ]; then
  echo "[-] Gemfile does not exist."
  exit 1
fi

# This might not work
if [ ! -d $REPO/Gemfile.lock ]; then
  echo "[-] Gemfile.lock does not exist."
  exit 1
fi

cd $REPO

if [ $(bundle list | wc -l) -lt 2 ]; then
    echo "[-] Less than 2 gems handled by bundler"
fi

echo "[+] Bundler set up correctly"
