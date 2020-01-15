import os
import sys
import subprocess
import signal
import time

# Doesn't work under Windows.
if os.name == 'nt':
    print('Python3 signalling on Windows does NOT work! Abort!')
    exit(-1)

ppid = os.getpid()
child = subprocess.Popen(['python3', 'signal-child.py'])
cpid = child.pid
print('<Parent-{:>6}>: Starting <Child-{:>6}>...\n'.format(ppid, cpid))
sys.stdout.flush()
print('<Parent-{:>6}>: Waiting for the <Child-{:>6}> to start...'.format(ppid, cpid))
sys.stdout.flush()
time.sleep(1)
os.kill(child.pid, signal.SIGUSR1)