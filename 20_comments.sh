#!/bin/bash

REPO=$1

SKELETON_COMMENTS=/tmp/comments

cat > $SKELETON_COMMENTS << EOF
  # TODO: Implement this method
  #
  # This method should return a two-dimensional array.
  # Each element of the array should be one of the
  # following values (These are "symbols", you can use
  # them like constant values):
  # :red
  # :blue
  # :green
  # :yellow
  # :cyan
  # :magenta
  #
  # It is important that this method is used because
  # this will be used for checking the functionality
  # of your implementation.
# TODO: Implement everything else as described in the
#       assignment brief.
EOF

COMMENTS=$(awk '{if (f==1) { r[$0] } else if (! ($0 in r)) { print $0 } } ' f=1 $SKELETON_COMMENTS f=2 $REPO/*.rb | grep -E ".*#[^\{].*$" | sed -e 's/^.*#//g' | wc -l)

if [ $COMMENTS -gt 10 ]; then
    echo "[+] Well documented code"
    rm $SKELETON_COMMENTS
    exit 0
else
    echo "[-] Not well documented code"
    rm $SKELETON_COMMENTS
    exit 1
fi
