#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


command = "ruby %s/floodit.rb" % (sys.argv[1])
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin"}
                                      })
fout = open('/tmp/floodit.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)
  # Main menu
  p.sendline("s")
  p.expect([re.compile('.*turns.*', re.IGNORECASE), pexpect.TIMEOUT], timeout=2)
  p.close()
except:
  print("[-] Main menu option to start game does not work correctly")
  sys.exit(1)

try:
  p = pexpect.spawn(command)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)

  # Change size
  p.sendline("c")
  p.expect(pexpect.TIMEOUT, timeout=2)
  p.sendline("5")
  p.expect(pexpect.TIMEOUT, timeout=2)
  p.sendline("5")
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)
except:
  print("[-] Main menu option to change size does not work correctly")
  sys.exit(1)

try:
  # Quiz
  p.sendline("q")
  p.expect(pexpect.EOF)
  print("[+] All menu options work correctly")
  sys.exit(0)
except SystemExit as e:
  raise
except:
  print("[-] Main menu option to quit does not work correctly")
  sys.exit(1)
  
fout.close()

