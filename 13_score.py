#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style
import shutil

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
  command = "ruby %s/floodit.rb" % sys.argv[1]
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
  fout = open('/home/codio/workspace/autograding_logs/13_score.log','wb')
  p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect([re.compile('turns', re.IGNORECASE), re.compile('attempts', re.IGNORECASE)], timeout=3)
except:
  print("[-] Could not check score calculation: No score displayed after game start")
  sys.exit(1)

try:
  x = int(re.sub(r'[^0-9]', "", p.after))
  if x != 0:
      print("[-] Score calculation does not start off with 0 turns")
      sys.exit(1)
except SystemExit as e:
  raise
except:
      print("[-] Score calculation does not start off with 0 turns")
      sys.exit(1)

try:
  p.sendline("r")
  p.expect([re.compile('turns', re.IGNORECASE), re.compile('attempts', re.IGNORECASE)], timeout=3)
except SystemExit as e:
  raise
except:
  print("[-] Could not check score calculation: No score displayed after one round")
  sys.exit(1)

try:
  x = int(re.sub(r'[^0-9]', "", p.after))
  if x != 1:
      print("[-] Score calculation does not increment turns: %d" % x)
      sys.exit(1)
except SystemExit as e:
  raise
except:
      print("[-] Score calculation does not increment turns: %s" % p.after)
      sys.exit(1)

try:
  p.sendline("b")
  p.expect([re.compile('turns', re.IGNORECASE), re.compile('attempts', re.IGNORECASE)], timeout=3)
except:
  print("[-] Could not check score calculation: No score displayed after game play")
  sys.exit(1)

x = int(re.sub(r'[^0-9]', "", p.after))
if x != 2:
      print("[-] Score calculation does not increment turns properly")
      sys.exit(1)

print("[+] Score calculation works properly")
fout.close()
