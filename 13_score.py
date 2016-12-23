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
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin"})
  fout = open('home/codio/workspace/autograding_logs/13_score.log','wb')
  p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect(re.compile('main menu', re.IGNORECASE), timeout=2)
  p.sendline("s")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
except:
  print("[-] Could not check score calculation: No score displayed after game start")
  sys.exit(1)

try:
  x = int(re.sub(r'[^0-9]', "", p.after))
  if x != 0:
      print("[-] Score calculation does not start off with 0 turns")
      sys.exit(1)
except:
      print("[-] Score calculation does not start off with 0 turns")
      sys.exit(1)

try:
  p.sendline("r")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
except:
  print("[-] Could not check score calculation: No score displayed after one round")
  sys.exit(1)

try:
  x = int(re.sub(r'[^0-9]', "", p.after))
  if x != 1:
      print("[-] Score calculation does not increment turns")
      sys.exit(1)
except:
      print("[-] Score calculation does not increment turns")
      sys.exit(1)

try:
  p.sendline("b")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
except:
  print("[-] Could not check score calculation: No score displayed after game play")
  sys.exit(1)

x = int(re.sub(r'[^0-9]', "", p.after))
if x != 2:
      print("[-] Score calculation does not increment turns properly")
      sys.exit(1)

print("[+] Score calculation works properly")
fout.close()
