#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


command = "ruby %s/floodit.rb" % sys.argv[1]
p = pexpect.spawn(command)
fout = open('/tmp/floodit.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  p.sendline("c")
  p.expect(re.compile('width', re.IGNORECASE), timeout=1)
  p.sendline("5")
  p.expect(re.compile('height', re.IGNORECASE), timeout=1)
  p.sendline("5")
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=1)
  exp = ""
  for i in range(5):
    for i in range(5):
      exp += Back.RED + "  " + Style.RESET_ALL
    exp += "\n"

  exp = exp.replace('\r\n', '+').replace('\n', '+')

  ansi_escape = re.compile(r'\x1b[^m]*m')
  output = p.before
  output = output.replace('\r\n', '+').replace('\n', '+')
  output = ansi_escape.sub('', output)
  exp    = ansi_escape.sub('', exp)


  if exp in output:
    print("[+] Setting size worked correctly")
  else:
    print("[-] Setting size did not work correctly")

except:
  print("[-] Setting size did not work correctly")
    
#fout.close()
