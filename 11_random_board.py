#!/usr/bin/env python

import pexpect
import re
import sys

command = "ruby %s/floodit.rb" % sys.argv[1]
p = pexpect.spawn(command)
p.sendline()
p.expect("Main menu")
p.sendline("s")
p.expect("Number of turns")
output1 = p.before
p.close()

command = "ruby %s/floodit.rb" % sys.argv[1]
p = pexpect.spawn(command)
p.sendline()
p.expect(re.compile('main menu', re.IGNORECASE))
p.sendline("s")
p.expect(re.compile('number of turns', re.IGNORECASE))
output2 = p.before
p.close()
print(output2)

if output1 == output2:
  print("[-] Board initialised with fixed values")
else:
  print("[+] Board initialised randomly")
