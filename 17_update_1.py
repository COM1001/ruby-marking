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
(0..8).each do |row| 
  (7..13).each do |i| 
    __ar[row][i] = :blue
  end
end
__ar[0][0] = :green
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
  p.expect(pexpect.TIMEOUT, timeout=1)

  p.sendline("r")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("b")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  print("[+] Game 1 played correctly")
except:
  print("[-] Game 1 not played correctly")
  sys.exit(1)


fout.close()

