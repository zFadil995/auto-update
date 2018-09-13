from subprocess import PIPE, run
from dateutil.parser import parse
import time

def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

while True:
    try:
        cmd("git fetch")
        local = parse(cmd("git log master").splitlines()[2][8:])
        origin = parse(cmd("git log origin/master").splitlines()[2][8:])
        if local < origin:
            cmd("git pull")
        elif local > origin:
            cmd("git push")
    except:
        print("Something went wrong!")
    time.sleep(300)
