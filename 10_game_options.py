#!/usr/bin/env python

import pexpect
import re
import sys
import shutil
from colorama import Back, Style

TMPDIR="/tmp/floodit_marking"
shutil.rmtree(TMPDIR, True)
shutil.copytree(sys.argv[1], TMPDIR)

workfile = "%s/floodit.rb" % TMPDIR
script = open("%s/floodit.rb" % sys.argv[1], 'r')
of = open(workfile, 'w')

of.write("""require 'mocha/api'
__ar = Array.new(9) { Array.new(14, :red) }
i = 0
colours = [ :red, :green, :blue, :yellow, :cyan, :magenta ]
current = 0
while i < 14*9 do
  row = i / 14
  col = i % 14
  __ar[row][col] = colours[current]
  current = (current + 1) % (colours.size)
  i += 1
end

stubs(:get_board).returns(__ar)
""")
of.write(script.read())
script.close()
of.close()


command = "ruby %s" % (workfile)
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
fout = open('/home/codio/workspace/autograding_logs/10_game_options.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=3)
except:
  print("[-] Game did not start, so could not check in-game options")
  sys.exit(1)

colours = ['g', 'b', 'y', 'c', 'm', 'r']
for c in colours:
  p.sendline(c)
  try:
      p.expect(re.compile('turns', re.IGNORECASE), timeout=3)
  except:
      print("[-] In-game options do not work correctly: Colour %s not accepted" % c)
      sys.exit(1)
    
try:
  p.sendline("q")
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  print("[+] In-game options work correctly")
except:
  print("[-] In-game options do not work correctly: Could not quit game")
  sys.exit(1)
  
fout.close()

