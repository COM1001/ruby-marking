#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


workfile = "/tmp/floodit_tmp.rb"
print(sys.argv[0])
script = open(sys.argv[1], 'r')
of = open(workfile, 'w')

of.write("""require 'mocha/api'
__ar = Array.new(9) { Array.new(14, :red) }
i = 0
colours = [ :red, :green, :blue, :yellow, :cyan, :magenta ]
current = 0
while i < 14*9 do
  row = i / 14
  col = i % 14
  __ar[row][col] = colours[current]
  current = (current + 1) % (colours.size)
  i += 1
end

stubs(:get_board).returns(__ar)
""")
of.write(script.read())
script.close()
of.close()


command = "ruby %s" % workfile
p = pexpect.spawn(command)
fout = open('/tmp/floodit.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect(re.compile('main menu', re.IGNORECASE))
  p.sendline("s")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  colours = ['r', 'g', 'b', 'y', 'c', 'm']
  current = 1
  i = 1
  while i < 30:
    row = i / 14
    col = i % 14
    p.sendline(colours[current])
    current = (current + 1) % len(colours)
    p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
    i += 1
    
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  print("[+] Game 3 played correctly")
except:
  print("[-] Game 3 not played correctly")

fout.close()

