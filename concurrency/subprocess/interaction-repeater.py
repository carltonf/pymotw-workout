import subprocess
import io

# write and read one by one
proc = subprocess.Popen(
    ['python', '-u', 'concurrency/repeater.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
)

proc_stdin = io.TextIOWrapper(
    proc.stdin,
    encoding = 'utf-8',
    line_buffering = True,
)

proc_stdout = io.TextIOWrapper(
    proc.stdout,
    encoding = 'utf-8'
)

for i in range(5):
    msg = "{}\n".format(i)
    proc_stdin.write(msg)
    print( proc_stdout.readline().rstrip() )

remainder = proc.communicate()[0].decode('utf-8')
print('Remainder:\n', remainder)

# write but read all at once
proc = subprocess.Popen(
    ['python', '-u', 'concurrency/repeater.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
)

proc_stdin = io.TextIOWrapper(
    proc.stdin,
    encoding = 'utf-8',
)

for i in range(5):
    msg = "%d\n" % i
    proc_stdin.write(msg)
# without the `flush`, it's likely 'remainder' would be empty.
proc_stdin.flush()

remainder = proc.communicate()[0].decode('utf-8')
print('Remainder:\n%s' % remainder)
