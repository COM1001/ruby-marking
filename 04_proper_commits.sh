#!/bin/bash

REPO=$1

if [ ! -d $REPO/.git ]; then
  echo "[-] no git repository, cannot check commits"
  exit 1
fi

cd $REPO

COMMITS=$(git log --oneline --no-merges  2>/dev/null | awk '{print $1}')

LINES_NECESSARY=5
SUBSTANTIAL_COMMITS=0

for COMMIT in $COMMITS; do
    CHANGE_SIZE=$(git diff --shortstat $COMMIT ${COMMIT}^1 2>/dev/null | awk '{print $4 + $6}')
    if [ -z "$CHANGE_SIZE" ]; then
      continue
    fi
    if [ "$CHANGE_SIZE" -gt $LINES_NECESSARY ]; then
	SUBSTANTIAL_COMMITS=$((SUBSTANTIAL_COMMITS+1))	
    fi
done

if [ "$SUBSTANTIAL_COMMITS" -lt 5 ]; then
  echo "[-] There are less than five commits with substantial changes."
  exit 1
fi

echo "[+] Found $COMMITS commits."
