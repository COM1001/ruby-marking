#!/usr/bin/env python

import pexpect
import re
import sys
from colorama import Back, Style
import time
import shutil

TMPDIR="/tmp/floodit_marking"
shutil.rmtree(TMPDIR, True)
shutil.copytree(sys.argv[1], TMPDIR)

workfile = "%s/floodit.rb" % TMPDIR

script = open("%s/floodit.rb" % sys.argv[1], 'r')
of = open(workfile, 'w')

of.write("""require 'mocha/api'
__ar = Array.new(9) { Array.new(14, :red) }
(0..8).each do |row| 
  (7..13).each do |i| 
    __ar[row][i] = :blue
  end
end
__ar[0][0] = :green
stubs(:get_board).returns(__ar)
""")
of.write(script.read())
script.close()
of.close()

try:
  command = "ruby %s" % workfile
  p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
  fout = open('/home/codio/workspace/autograding_logs/14_completion.log','wb')
  p.logfile = fout
  p.setecho(True)
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)])
  p.sendline("s")
  time.sleep(1) # seems this can be too quick for the number to appear...
  p.expect(re.compile('completion.*', re.IGNORECASE), timeout=3)
except:
  print("[-] Failed to check for completion - no completion displayed initially")
  sys.exit(1)

try:
  x = float(re.sub(r'[^0-9\.]', "", p.after))
  if x > 1.0:
    print("[-] Completion calculation does not work")
    sys.exit(1)
except SystemExit as e:
  raise
except:
    print("[-] Completion calculation does not work")
    sys.exit(1)
  
    
try:
  p.sendline("r")
  time.sleep(1) # seems this can be too quick for the number to appear...
  p.expect(re.compile('completion.*', re.IGNORECASE), timeout=3)
except:
  print("[-] Failed to check for completion - no completion displayed after one round")
  sys.exit(1)

try:
  x = float(re.sub(r'[^0-9\.]', "", p.after))
  if x != 50.0:
    print("[-] Completion calculation does not work")
    sys.exit(1)
except SystemExit as e:
  raise
except:
    print("[-] Completion calculation does not work")
    sys.exit(1)
  
try:
  p.sendline("b")
  time.sleep(1) # seems this can be too quick for the number to appear...
  value = p.expect([re.compile('completion.*', re.IGNORECASE), re.compile('.*won.*', re.IGNORECASE)], timeout=3)

  if value == 0:
      x = float(re.sub(r'[^0-9\.]', "", p.after))
      if x != 100.0:
        print("[-] Completion calculation does not work")
        sys.exit(1)
  print("[+] Completion calculation is working")
  
except SystemExit as e:
  raise
except:
  print("[-] Failed to check for completion - no completion displayed at end")
  sys.exit(1)


fout.close()
