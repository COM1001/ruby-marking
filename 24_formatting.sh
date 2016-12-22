#!/bin/bash

REPO=$1
GEM_HOME=/home/codio/.gems
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

OUTPUT=$(rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines,Style/SpaceInsideBrackets,SpaceInsideBrackets,Tab -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Source code is formatted according to style guide"
    exit 0
else
    echo "[-] Source code is not formatted according to style guide. Here is the output of Rubocop:"
    rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines -D $REPO/floodit.rb
    exit 1
fi

#SpaceInsideParens,SpaceAroundOperators,RedundantParentheses,EmptyLinesAroundMethodBody,NilComparison,NonNilCheck,GuardClause,Next,IndentationWidth,RedundantReturn
