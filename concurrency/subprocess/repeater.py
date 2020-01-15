# repeater.py
import os
import sys

fname = os.path.basename(__file__)

sys.stderr.writelines('%s started:\n' % fname)
sys.stderr.flush

while True:
    line = sys.stdin.readline()
    sys.stderr.flush()
    # Until EOF or empty input
    if not ( line and line.strip() ) :
        break
    sys.stdout.writelines(line)
    sys.stdout.flush()

sys.stderr.writelines('%s terminated.\n' % fname)
sys.stderr.flush()