#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


command = "ruby %s/floodit.rb" % sys.argv[1]
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin"})
fout = open('/home/codio/workspace/autograding_logs/16_sizes.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE)], timeout=2)
  p.sendline("c")
  p.expect(pexpect.TIMEOUT, timeout=2)
  p.sendline("10")
  p.expect(pexpect.TIMEOUT, timeout=2)
  p.sendline("10")
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE)], timeout=2)
  p.sendline("s")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  exp = ""
  for i in range(10):
    for j in range(10):
      exp += Back.RED + "  " + Style.RESET_ALL
    exp += "+"

  ansi_escape = re.compile(r'\x1b[^m]*m')
  output = p.before
  output = output.replace('\r\n', '+').replace('\n', '+')
  output = ansi_escape.sub('', output)
  exp    = ansi_escape.sub('', exp)


  if exp in output:
    print("[+] Setting size worked correctly")
  else:
    print("[-] Setting size did not work correctly")
    sys.exit(1)
    
except SystemExit as e:
  raise
except:
  print("[-] Setting size did not work correctly")
  sys.exit(1)
  
#fout.close()
