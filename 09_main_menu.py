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
  # Main menu
  p.sendline("s")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=1)
  p.sendline("q")
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)

  # Change size
  p.sendline("c")
  p.expect(re.compile('width', re.IGNORECASE), timeout=1)
  p.sendline("5")
  p.expect(re.compile('height', re.IGNORECASE), timeout=1)
  p.sendline("5")
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)

  # Quiz
  p.sendline("q")
  p.expect(pexpect.EOF)
  print("[+] All menu options work correctly")
except:
  print("[-] Main menu options do not work correctly")

fout.close()

