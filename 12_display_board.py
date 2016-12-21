#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style

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
  p = pexpect.spawn(command)
  #fout = open('/tmp/floodit.log','wb')
  #p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE))
  p.sendline("s")
  p.expect(re.compile('number of turns', re.IGNORECASE), timeout=1)

  output = p.before
  ansi_escape = re.compile(r'\x1b[^m]*m \x1b\[0m')
  output = ansi_escape.sub('G', output)

  p.close()

  str = Back.GREEN + "  " + Style.RESET_ALL
  str = Back.BLUE + "  " + Style.RESET_ALL
  for i in range(12):
    str += Back.RED + "  " + Style.RESET_ALL
  str += "\n"
  for i in range(8):
    for i in range(14):
      str += Back.RED + "  " + Style.RESET_ALL
    str += "\n"

  str    = str.replace('\r\n', '').replace('\n', '')
  output = output.replace('\r\n', '').replace('\n', '')


  if str in output:
    print("[+] Correct display of board")
  else:
    print("[-] Board is not displayed correctly")

except:
  print("[-] Could not check board display")

#fout.close()
