#!/usr/bin/env python
#!/usr/bin/env python
#
import shlex
import os
from glob import glob
from subprocess import run, check_call, check_output, CalledProcessError, PIPE

# ls -l DATA/*.txt

cmd = "ls -l"
files = "DATA/*.txt"

raw_cmd = cmd.split()
file_list = glob(files)

full_cmd = raw_cmd + file_list + ["wombat"]
print(full_cmd)

proc = run(full_cmd, stdout=PIPE, stderr=PIPE)

output = proc.stdout.decode()
print()

print(output)

print(proc.stderr.decode())
