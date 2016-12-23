#!/bin/bash

REPO=$1
export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems:/home/codio/.gem/ruby/2.2.0:/var/lib/gems/2.2.0:/usr/share/rubygems-integration/2.2.0:/usr/share/rubygems-integration/all
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

gem install rubocop --conservative > /dev/null 2>&1

OUTPUT=$(rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines,Style/SpaceInsideBrackets,SpaceInsideBrackets,Tab,GlobalVars -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Source code is formatted according to style guide"
    exit 0
else
    echo "[-] Source code is not formatted according to style guide. Here is the output of Rubocop:"
    rubocop --only Style --except StringLiterals,ConstantName,MethodName,PredicateName,VariableName,Style/LeadingCommentSpace,Style/TrailingWhitespace,Style/EmptyLines -D $REPO/floodit.rb
    exit 1
fi

#SpaceInsideParens,SpaceAroundOperators,RedundantParentheses,EmptyLinesAroundMethodBody,NilComparison,NonNilCheck,GuardClause,Next,IndentationWidth,RedundantReturn
