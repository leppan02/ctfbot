#!/usr/bin/expect -f
spawn ssh muppbot@213.64.176.135
expect "assword:"
send " \r"
interact
