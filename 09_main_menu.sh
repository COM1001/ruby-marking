#!/bin/bash

REPO=/home/codio/workspace/flood-it
SCRIPT=$REPO/floodit.rb
TMP_SCRIPT=/tmp/floodit_tmp.rb

# 

cat $TMP_SCRIPT | sed -e 's/^.*\.splash/p get_board(10,10); exit 1/' > $TMP_SCRIPT

# Test 'q'

# Test 'c'

# Test 's'

