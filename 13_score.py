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
  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command)
  #fout = open('/tmp/floodit.log','wb')
  #p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=2)

  regex = re.compile('.*turns:', re.IGNORECASE)
  x = int(re.sub("[^0-9]", "", re.sub(regex, "", p.after)))
  if x != 0:
      print("[-] Score calculation does not start off with 0 turns")
      sys.exit(1)
  p.sendline("r")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  x = int(re.sub(regex, "", p.after))
  if x != 1:
      print("[-] Score calculation does not increment turns")
      sys.exit(1)
  p.sendline("b")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  x = int(re.sub(regex, "", p.after))
  if x != 2:
      print("[-] Score calculation does not increment turns properly")
      sys.exit(1)

  print("[+] Score calculation works properly")
  sys.exit(0)
except SystemExit as e:
  raise
except:
  print("[-] Could not check score calculation")
  sys.exit(1)
