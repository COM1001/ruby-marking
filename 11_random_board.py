#!/usr/bin/env python

import pexpect
import re
import sys

try:
  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=1)
  output1 = p.before
  p.close()

  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=1)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=1)
  output2 = p.before
  p.close()

  if output1 == output2:
    print("[-] Board initialised with fixed values")
  else:
    print("[+] Board initialised randomly")
except:
    print("[-] Could not check board initialisation")
