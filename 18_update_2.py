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
(0..13).each do |i| 
  __ar[1][i] = :blue
  __ar[2][i] = :blue
  __ar[3][i] = :green
  __ar[4][i] = :green
  __ar[5][i] = :cyan
  __ar[6][i] = :cyan
  __ar[7][i] = :magenta
  __ar[8][i] = :yellow
end
stubs(:get_board).returns(__ar)
""")
of.write(script.read())
script.close()
of.close()


command = "ruby %s" % workfile
p = pexpect.spawn(command, env = {"GEM_HOME": "/home/codio/.gems", "GEM_PATH": "/home/codio/.gems", "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/codio/.gems/bin", "TERM": "linux"})
fout = open('/home/codio/workspace/autograding_logs/18_update_2.log','wb')
p.logfile = fout
p.setecho(True)
p.sendline()
try:
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)])
  p.sendline("s")
  p.expect(pexpect.TIMEOUT, timeout=2)

  p.sendline("b")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  p.sendline("g")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  p.sendline("c")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  p.sendline("m")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  p.sendline("y")
  p.expect(re.compile('.*turns.*', re.IGNORECASE), timeout=2)
  p.sendline()
  p.expect([re.compile('main.* menu', re.IGNORECASE), re.compile('s.*=.*start game', re.IGNORECASE), re.compile('start game.*:.*s', re.IGNORECASE), re.compile('m.*a.*i.*n.*m.*e.*n.*u', re.IGNORECASE)], timeout=2)
  print("[+] Board updating test scenario 2 played correctly")
except:
  print("[-] Board updating test scenario 2 not played correctly")
  sys.exit(1)

fout.close()
