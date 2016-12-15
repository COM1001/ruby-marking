#!/bin/bash

REPO=/home/codio/workspace/flood-it

if [ ! -d $REPO/.git ]; then
  echo ".git directory does not exist."
  exit 1
fi

cd $REPO
FILES=$(git ls-files 2>/dev/null)

git ls-files floodit.rb --error-unmatch >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "[-] File floodit.rb is not in the repository!"
  exit 1
fi

git diff --cached --exit-code > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "[-] There are staged changes that have not been committed."
  exit 1
fi

CHANGES=$(git diff --name-only floodit.rb)
if [ ! -z "$CHANGES" ]; then
  echo "[-] There are changes to floodit.rb but the file has not been staged for commit yet."
  exit 1
fi


echo "[+] floodit.rb is in the repository and the repository is in a clean state"
