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

try:
  command = "ruby %s" % workfile
  p = pexpect.spawn(command)
  #fout = open('/tmp/floodit.log','wb')
  #p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE))
  p.sendline("s")
  p.expect(re.compile('.*completion.*', re.IGNORECASE), timeout=1)

  regex = re.compile('.*completion:', re.IGNORECASE)
  x = float(re.sub(regex, "", p.after).replace("%", ""))
  if x >= 1.0:
    print("[-] Completion calculation does not work")
    sys.exit(1)
  p.sendline("r")
  p.expect(re.compile('completion.*', re.IGNORECASE), timeout=1)
  x = float(re.sub(regex, "", p.after).replace("%", ""))
  if x != 50.0:
    print("[-] Completion calculation does not work")
    sys.exit(1)
  p.sendline("b")
  p.expect(re.compile('completion.*', re.IGNORECASE), timeout=1)
  x = float(re.sub(regex, "", p.after).replace("%", ""))
  if x != 100.0:
    print("[-] Completion calculation does not work")
    sys.exit(1)

  print("[+] Completion calculation is working")

except SystemExit as e:
  raise
except:
  print("[-] Failed to check for completion")
  sys.exit(1)
#fout.close()
