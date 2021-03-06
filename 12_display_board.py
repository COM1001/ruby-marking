#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style
import shutil



def get_colorama_str():
  str = Back.GREEN + "  " + Style.RESET_ALL
  str += Back.BLUE + "  " + Style.RESET_ALL
  for i in range(12):
    str += Back.RED + "  " + Style.RESET_ALL
  for i in range(8):
    for i in range(14):
      str += Back.RED + "  " + Style.RESET_ALL

  return str


TMPDIR="/tmp/floodit_marking"
shutil.rmtree(TMPDIR, True)
shutil.copytree(sys.argv[1], TMPDIR)

workfile = "%s/floodit.rb" % TMPDIR

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


try:
  command = "ruby %s" % workfile
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems",
                                  "GEM_PATH": "/home/codio/.gems",
                                  "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
  fout = open('/home/codio/workspace/autograding_logs/12_display_board.log','wb')
  p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect(re.compile('turns', re.IGNORECASE), timeout=3)

  output = p.before
  p.close()
except:
  output = p.before
  p.close()

 
str = get_colorama_str()
output = output.replace('\r\n', '').replace('\n', '').replace('0;39;', '')

if str in output:
  print("[+] Correct display of board")
  sys.exit(0)
else:
  try:
    command = "ruby %s/floodit.rb" % sys.argv[1]
    p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems",
                                  "GEM_PATH": "/home/codio/.gems",
                                  "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
    fout = open('/home/codio/workspace/autograding_logs/12_display_board.log','wb')
    p.logfile = fout
    p.setecho(True)
    p.sendline()
    p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
    p.sendline("s")
    p.expect(re.compile('turns', re.IGNORECASE), timeout=3)

    output = p.before
    p.close()
  except:
    output = p.before
    p.close()

  output = output.replace('\r\n', '').replace('\n', '').replace('0;39;', '')
  ansi_escape = re.compile(r'\x1b[^m]*m')
  output = ansi_escape.sub('X', output)
  str = ansi_escape.sub('X', str)
  
  if str in output:
    print("[+] Correct display of board, although get_board did not work")
    sys.exit(0)
  else:
    print("[-] Board is not displayed correctly")
    sys.exit(1)


fout.close()

