#!/bin/bash

REPO=$1
export GEM_HOME=/home/codio/.gems
export GEM_PATH=/home/codio/.gems:/home/codio/.gem/ruby/2.2.0:/var/lib/gems/2.2.0:/usr/share/rubygems-integration/2.2.0:/usr/share/rubygems-integration/all
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin

gem list | grep -q bundler

if [ $? -ne 0 ]; then
    gem install bundler > /dev/null 2>&1
fi

if [ ! -e $REPO/Gemfile ]; then
  echo "[-] Gemfile does not exist."
  exit 1
fi

# This might not work
if [ ! -e $REPO/Gemfile.lock ]; then
  echo "[-] Gemfile.lock does not exist."
  # Make sure bundle is installed anyway
  bundle install > /dev/null 2>&1
  exit 1
fi

cd $REPO

if [ $(bundle list | wc -l) -lt 2 ]; then
    echo "[-] Less than 2 gems handled by bundler"
fi

echo "[+] Bundler set up correctly"

# Make sure bundle is installed anyway
bundle install > /dev/null 2>&1
