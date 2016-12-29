#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style


def get_colorama_str():
  str = Back.GREEN + "  " + Style.RESET_ALL
  str += Back.BLUE + "  " + Style.RESET_ALL
  for i in range(12):
    str += Back.RED + "  " + Style.RESET_ALL
  for i in range(8):
    for i in range(14):
      str += Back.RED + "  " + Style.RESET_ALL

  return str

command = "ruby %s/floodit.rb" % sys.argv[1]

p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"})
fout = open('/home/codio/workspace/autograding_logs/09_main_menu.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main menu', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  # Main menu
  p.sendline("s")
  p.expect([re.compile('turns', re.IGNORECASE), pexpect.TIMEOUT], timeout=3)
  p.close()
except:
  output = p.before
  str = get_colorama_str()
  output = output.replace('\r\n', '').replace('\n', '').replace('0;39;', '')
  # Don't check actual contents
  ansi_escape = re.compile(r'\x1b[^m]*m')
  output = ansi_escape.sub('X', output)
  str = ansi_escape.sub('X', str)

  if not str in output:
    print("[-] Main menu option to start game does not work correctly")
    sys.exit(1)

try:
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"})
  p.logfile = fout
  p.sendline()
  p.expect([re.compile('main menu', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)

  # Change size
  p.sendline("c")
  p.expect(pexpect.TIMEOUT, timeout=3)
  p.sendline("5")
  p.expect(pexpect.TIMEOUT, timeout=3)
  p.sendline("5")
  r = p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE), pexpect.TIMEOUT], timeout=3)
  if r == 4:
    # Some people want to have an additional keypress here...
    p.sendline()
    p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.close()

except:
  print("[-] Main menu option to change size does not work correctly")
  sys.exit(1)

try:
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"})
  p.logfile = fout
  p.sendline()
  p.expect([re.compile('main menu', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("q")
  p.expect(pexpect.EOF)
  print("[+] All menu options work correctly")
except:
  print("[-] Main menu option to quit does not work correctly")
  sys.exit(1)
  
fout.close()
