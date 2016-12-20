#!/bin/bash

REPO=/home/codio/workspace/flood-it
SCRIPT=$REPO/floodit.rb
TMP_SCRIPT=/tmp/floodit_tmp.rb

# 

cat $TMP_SCRIPT | sed -e 's/^.*\.splash/exit 1/' > $TMP_SCRIPT

ruby -e "load $TMP_SCRIPT" scripts/test_board_initialised.rb
