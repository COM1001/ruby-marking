#!/bin/bash

REPO=$1
export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems:/home/codio/.gem/ruby/2.2.0:/var/lib/gems/2.2.0:/usr/share/rubygems-integration/2.2.0:/usr/share/rubygems-integration/all
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

RUBOCOP_FILE=/tmp/rubocop_tmp.yml
echo "Metrics/MethodLength:" > $RUBOCOP_FILE
echo "  Max: 30" >> $RUBOCOP_FILE
echo >> $RUBOCOP_FILE
echo "Style/GlobalVars:" >> $RUBOCOP_FILE
echo "  AllowedVariables:" >> $RUBOCOP_FILE
echo "    - '\$COLOURS'" >> $RUBOCOP_FILE
echo "    - '\$COLORS'" >> $RUBOCOP_FILE
echo "    - '\$COLOUR_HASH'" >> $RUBOCOP_FILE

gem install rubocop --conservative > /dev/null 2>&1

OUTPUT=$(rubocop -c $RUBOCOP_FILE --only MethodLength,GlobalVars -D $REPO/floodit.rb)

if [ $? -eq 0 ]; then
    echo "[+] Well modularised code"
    rm $RUBOCOP_FILE
    exit 0
else
    echo "[-] Not well modularised code. Check the Rubocop output in /home/codio/workspace/autograding_logs/22_modularised.log"
    rubocop -c $RUBOCOP_FILE --only MethodLength,GlobalVars -D $REPO/floodit.rb > /home/codio/workspace/autograding_logs/22_modularised.log
    rm $RUBOCOP_FILE
    exit 1
fi


