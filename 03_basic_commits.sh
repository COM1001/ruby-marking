#!/bin/bash

REPO=/home/codio/workspace/flood-it

if [ ! -d $REPO/.git ]; then
  echo ".git directory does not exist."
  exit 1
fi

cd $REPO

COMMITS=$(git log --oneline  2>/dev/null | wc -l)

if [ "$COMMITS" -lt 5 ]; then
  echo "[-] There are less than five commits."
  exit 1
fi

echo "[+] Found $COMMITS commits."
