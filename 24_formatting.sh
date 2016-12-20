#!/bin/bash

REPO=$1

OUTPUT=$(rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines,Style/SpaceInsideBrackets,SpaceInsideBrackets -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Source code is formatted according to style guide"
    exit 0
else
    echo "[-] Source code is not formatted according to style guide:"
    rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines -D $REPO/floodit.rb
    exit 1
fi

