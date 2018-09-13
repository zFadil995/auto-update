from subprocess import PIPE, run
import time

def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

try:
    local = cmd("git log --oneline master")
    origin = cmd("git log --oneline origin/master")

    if local[0:7] != origin[0:7]:
        print("IN")
except:
    print("Something went wrong!")