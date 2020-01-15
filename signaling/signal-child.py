import os
import sys
import signal
import time

pid = os.getpid()
proc_name = '<Proc-{:>6}>'.format(pid)
received = False

# NOTE on Windows, SIGUSR1 doesn't exists
# See
# https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/signal?view=vs-2019#remarks
# Here I'm using SIGINT (i.e. Ctrl-c)
# UPDATE: the above doesn't work. Trying to send the SIGINT get a 'permission
# denied' error. This signalling test will only be done in Linux
if os.name == 'nt':
    print('Python3 signalling on Windows does NOT work! Abort!')
    exit(-1)

def sighandler_SIGUSR1(signum, frame):
    'Callback is invoked when a signal is received.'
    print('{}: Received signal SIGUSR1'.format(proc_name))
    sys.stdout.flush()
    global received
    received = True

print('{}>: Setting up signal handler...'.format(proc_name))
sys.stdout.flush()
signal.signal(signal.SIGUSR1, sighandler_SIGUSR1)
print('{}: Waiting for signal...'.format(proc_name))
sys.stdout.flush()
time.sleep(3)

if not received:
    print('{}: No signal received till the end.'.format(proc_name))
    sys.stdout.flush()