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

workfile = "/tmp/floodit_tmp.rb"
script = open("%s/floodit.rb" % sys.argv[1], 'r')
of = open(workfile, 'w')

of.write("""require 'mocha/api'
__ar = Array.new(9) { Array.new(14, :red) }
__ar[0][0] = :green
__ar[0][1] = :blue
stubs(:get_board).returns(__ar)
""")
of.write(script.read())
script.close()
of.close()

command = "ruby %s" % workfile

p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux"})
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
  if not str in output:
    print("[-] Main menu option to start game does not work correctly")
    sys.exit(1)

try:
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux"})
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
