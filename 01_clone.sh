#!/bin/bash

REPO=$1

if [ ! -d $REPO/.git ]; then
  echo "[-] Git repository does not exist."
  exit 1
fi

cd $REPO
if git log | grep -q b75e6660dd92d8fd5dd8f2be3a99122cf89d1281; then
    echo "[+] Found commit b75e666, so assuming you cloned the right repo"
else
    echo "[-] Did not find commit b75e666, you did not clone the right repo"
fi
