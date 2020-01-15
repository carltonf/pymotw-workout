# sending signal to a subprocess without knowing the id
import os
import subprocess
import sys
import time
import signal
import tempfile

if os.name == 'nt':
    print('os.setpgrp is NOT available on Windows. Abort!')
    exit(-1)


def setting_pgrp():
    print('Setting process group...')
    sys.stdout.flush()
    # NOTE os.setpgrp makes the current process the head of its pgrp and thus
    # the process group is named using the same id of pid of the current
    # process.
    os.setpgrp()
    print('The current process group is now', os.getpgrp())
    sys.stdout.flush()

script='''
echo "Message from the subshell <Proc - $$>"
set -x
python3 signal-child.py
'''

# TODO what wt means
scriptfile = tempfile.NamedTemporaryFile('wt')
script_fn = scriptfile.name
scriptfile.write(script)
# flush call is necessary without closing the file
scriptfile.flush()

# NOTE according to doc, 'preexec_fn' is not safe in multi-thread env and thus
# probably not recommended for use.
proc = subprocess.Popen(['sh', script_fn], preexec_fn=setting_pgrp)
proc_name = '<Parent-{:>6}>'.format(proc.pid)
print('{}: Waiting for the child of <Proc-{:>6}> to start...'.format(
    proc_name, proc.pid))
sys.stdout.flush()

time.sleep(1)

print('{}: Sending signal to child...'.format(proc_name))
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)

scriptfile.close()