#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess run function to run "ls -l" and print the output.

 b. Do the same as a), but don't print anything to the screen.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""
import subprocess

print("a.")
subprocess.run(['ls', '-l'])

print("b.")
subprocess.Popen(['ls', '-l'], stdout=None)

print("c. -- errors output")
try:
    subprocess.Popen(['/bogus/command'], stdout=subprocess.PIPE)
except OSError as e:
    print(e)

print("d.")
with subprocess.Popen(['du', '-h'], stdout=subprocess.PIPE) as proc:
    print(proc.stdout.read())

print("e.")
def commander(args):
    for arg in args:
        p = subprocess.run(arg, shell=True)
        print('Output for command: {} \n{}'.format(arg, p.stdout))

commander(['ls -l', 'who', 'whoami'])



