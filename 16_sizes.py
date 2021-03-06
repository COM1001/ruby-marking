#!/usr/bin/env python

import pexpect
import re
import sys
import shutil
from colorama import Back, Style


command = "ruby %s/floodit.rb" % sys.argv[1]
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = sys.argv[1])
fout = open('/home/codio/workspace/autograding_logs/16_sizes.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("c")
  p.expect(pexpect.TIMEOUT, timeout=3)
  p.sendline("10")
  p.expect(pexpect.TIMEOUT, timeout=3)
  p.sendline("10")
  r = p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE), pexpect.TIMEOUT], timeout=3)
  if r == 4:
    p.sendline()
    p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect(re.compile('turns', re.IGNORECASE), timeout=3)
  output = p.before
except:
  output = p.before

exp = ""
for i in range(10):
    for j in range(10):
      exp += Back.RED + "  " + Style.RESET_ALL
    exp += "+"

ansi_escape = re.compile(r'\x1b[^m]*m')
output = output.replace('\r\n', '+').replace('\n', '+')
output = ansi_escape.sub('', output)
exp    = ansi_escape.sub('', exp)


if exp in output:
  print("[+] Setting size worked correctly")
else:
  print("[-] Setting size did not work correctly")
  sys.exit(1)
    
fout.close()
