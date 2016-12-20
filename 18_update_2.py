#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


workfile = "/tmp/floodit_tmp.rb"
script = open("%s/floodit.rb" % sys.argv[1], 'r')
of = open(workfile, 'w')

of.write("""require 'mocha/api'
__ar = Array.new(9) { Array.new(14, :red) }
(0..13).each do |i| 
  __ar[1][i] = :blue
  __ar[2][i] = :blue
  __ar[3][i] = :green
  __ar[4][i] = :green
  __ar[5][i] = :cyan
  __ar[6][i] = :cyan
  __ar[7][i] = :magenta
  __ar[8][i] = :yellow
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

  p.sendline("b")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("g")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("c")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("m")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("y")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  print("[+] Game 2 played correctly")
except:
  print("[-] Game 2 not played correctly")


fout.close()
