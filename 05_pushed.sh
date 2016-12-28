#!/bin/bash

REPO=$1

if [ ! -d $REPO/.git ]; then
  echo "[-] no git repository, cannot check if everything is pushed."
  exit 1
fi

cd $REPO
FILES=$(git ls-files 2>/dev/null)

git ls-files floodit.rb --error-unmatch >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "[-] File floodit.rb is not in the repository, so can't check if the remote repo is ok."
  exit 1
fi

git diff --cached --exit-code > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "[-] There are staged changes that have not been committed."
  exit 1
fi


CHANGES=$(git diff --name-only floodit.rb)

if [ ! -z "$CHANGES" ]; then
  echo "[-] There are changes to hangman.rb but the file has not been staged for commit yet."
  exit 1
fi

# Check 1: origin should now point to compscishef
ORIGIN=$(git remote get-url origin)

if [ $? -ne 0 ]; then
  echo "[-] Remote origin has not been set."
  exit 1
fi

if $(echo $ORIGIN | grep -q "https://github.com/COM1001/flood-it"); then
  echo "[-] Your origin is still the original GitHub repository, not your own."
  exit 1
fi

# Check 2: origin and master should be in sync
UNPUSHED=$(git cherry 2>/dev/null | wc -l)
if [ $UNPUSHED -ne 0 ]; then
  echo "[-] It appears you did not push your local changes."
  exit 1
fi

echo "[+] All changes have been pushed to the remote repository."
