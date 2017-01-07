#!/usr/bin/env python

import pexpect
import re
import sys

try:
  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = sys.argv[1])
  fout = open('/home/codio/workspace/autograding_logs/11_random_board.log','wb')
  p.logfile = fout
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect([pexpect.TIMEOUT, pexpect.EOF], timeout=3)
  output1 = p.before
  p.close()

  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = sys.argv[1])
  p.logfile = fout
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect([pexpect.TIMEOUT, pexpect.EOF], timeout=3)
  output2 = p.before
  p.close()

  if output1 == output2:
    print("[-] Board initialised with fixed values")
    sys.exit(1)
  else:
    print("[+] Board initialised randomly")
except SystemExit as e:
  raise
except:
    print("[-] Could not check board initialisation")
    sys.exit(1)
