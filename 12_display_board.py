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


try:
  command = "ruby %s" % workfile
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems"})
  fout = open('/tmp/floodit.log','wb')
  p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=2)

  output = p.before

  p.close()

 
  str = get_colorama_str()
  output = output.replace('\r\n', '').replace('\n', '').replace('0;39;', '')

  if str in output:
    print("[+] Correct display of board")
    sys.exit(0)
  else:
    print("[-] Board is not displayed correctly")
    sys.exit(1)

except SystemExit as e:
  raise
except:
  print("[-] Could not check board display")
  sys.exit(1)

fout.close()

