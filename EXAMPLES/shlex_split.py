#!/usr/bin/env python
#
import shlex
import os
from glob import glob
from subprocess import run, check_call, check_output, CalledProcessError, PIPE

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # <1>

print(cmd.split())  # <2>
print()

print(shlex.split(cmd))  # <3>
os.system("whoami")
with os.popen('whoami') as who_in:
    print(who_in.read())

#  ls -l DATA/*.txt

cmd = "ls -l"
files = "../DATA/*.txt"

raw_cmd = cmd.split()
file_list = glob(files)

full_cmd = raw_cmd + file_list
print(full_cmd)
