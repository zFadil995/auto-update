from subprocess import PIPE, run
import time

def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

try:
    local = cmd("git log master")
    origin = cmd("git log origin/master")
    print(local.splitlines()[0])
    print(origin.splitlines()[0])    
except:
    print("Something went wrong!")