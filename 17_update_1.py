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


command = "ruby %s" % workfile
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux", "HOME" : "/home/codio"}, cwd = TMPDIR)
fout = open('/home/codio/workspace/autograding_logs/17_update_1.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)])
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=3)

  p.sendline("r")
  p.expect([re.compile('turns', re.IGNORECASE), re.compile('attempts', re.IGNORECASE)], timeout=3)
  p.sendline("b")
  p.expect([re.compile('turns', re.IGNORECASE), re.compile('attempts', re.IGNORECASE)], timeout=3)
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=3)
  print("[+] Board updating test scenario 1 worked correctly")
except:
  print("[-] Board updating test scenario 1 not played correctly")
  sys.exit(1)


fout.close()

