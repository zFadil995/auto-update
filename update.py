from subprocess import PIPE, run
from dateutil.parser import parse
import time

def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

try:
    cmd("git fetch")

    local = parse(cmd("git log master").splitlines()[2][8:])
    origin = parse(cmd("git log origin/master").splitlines()[2][8:])
    if local < origin:
        print("ORIGIN")
    elif local > origin:
        print("LOCAL")
    else:
        print("SAME")

except:
    print("Something went wrong!")