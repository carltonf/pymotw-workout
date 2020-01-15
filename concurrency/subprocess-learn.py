import subprocess


## Without check argument, it's essentially 'call'
completed = subprocess.run(['ls', '-l'])
print('returncode:', completed.returncode)

# NOTE on Windows, the Shell is cmd
completed = subprocess.run('echo %HOME%', shell=True)
print('returncode:', completed.returncode)

## check_call
try:
    completed = subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)

## Capturing the output
try:
    completed = subprocess.run('ls -l', check=True, stdout = subprocess.PIPE)
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout:\n{}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8')
    ))
except subprocess.CalledProcessError as err:
    print('ERROR:', err)

## Capturing the stderr
try:
    completed = subprocess.run(
        # NOTE in batch, use '&' to connect two commands in one line
        'echo to stdout & echo to stderr by redirection 1>&2',
        check = True,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout:\n{}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'),
    ))
    print('Have {} bytes in stderr:\n{}'.format(
        len(completed.stderr),
        completed.stderr.decode('utf-8'),
    ))

# Suppressing Output
try:
    completed = subprocess.run(
        'echo to stdout & echo to stderr 1>&2; exit 1',
        shell = True,
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('stdout is: {!r}'.format(completed.stdout))
    print('stderr is: {!r}'.format(completed.stderr))

# The functions run(), call(), check_call(), and check_output() are wrappers
# around the Popen class. More control can be attained by using Popen directly.
# We can mimic os.popen behaviors.

print('read:')
proc = subprocess.Popen(
    ['echo', 'to stdout'],
    stdout = subprocess.PIPE,
)
stdout_val = proc.communicate()[0].decode('utf-8')
print('stdout is', repr(stdout_val))

print('write:')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin = subprocess.PIPE,
)
proc.communicate('echo to stdin\n'.encode('utf-8'))

print('bi-directional i/o (popen2):')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
)
input = 'from stdin to stdout'.encode('utf-8')
output_val = proc.communicate(input)[0].decode('utf-8')
print('result:', repr(output_val))

print('capturing stderr (popen3):')
proc = subprocess.Popen(
    # NOTE actually we have troubles in following 'cat -' with other cmds.
    # i.e. 'cat - ;& echo to stderr 1>&2' doesn't work.
    # So let cat generate a real error instead
    "cat - non-existent-file",
    shell = True,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
)
msg = 'from stdin to stderr followed by errors'.encode('utf-8')
stdout_val, stderr_val = proc.communicate(msg)
print( 'stdout:', repr(stdout_val.decode('utf-8')) )
print( 'stderr:', repr(stderr_val.decode('utf-8')) )

print('stdin and stderr redirections:')
proc = subprocess.Popen(
    "cat - non-existent-file",
    stdin = subprocess.PIPE,
    # i.e. 1>&2
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT,
)
msg = 'from stdin AND stderr to stdout.'.encode('utf-8')
stdout_res, stderr_res = proc.communicate( msg )
if stdout_res:
    print('stdout:', repr(stdout_res.decode('utf-8')))
else:
    print('stdout:', repr(stdout_res))
if stderr_res:
    print('stderr:', repr(stderr_res.decode('utf-8')))
else:
    print('stderr:', repr(stderr_res))

## 2019-12-24: after serious try, I failed to redirect stderr to stdout
# import sys
# # If args is a string, the interpretation is platform-dependent and described
# # below. So the verdict is USE string sequence.
# proc = subprocess.Popen(
#     [ 'cat', '-', 'non-existent-file' ],
#     stdin = subprocess.PIPE,
#     stdout = sys.stderr.buffer,
#     stderr = subprocess.PIPE,
# )
# msg = 'from stdout to stderr.'.encode('utf-8')
# stdout_res, stderr_res = proc.communicate(msg)
# if stdout_res:
#     print('stdout:', repr(stdout_res.decode('utf-8')))
# else:
#     print('stdout:', repr(stdout_res))
# if stderr_res:
#     print('stderr:', repr(stderr_res.decode('utf-8')))
# else:
#     print('stderr:', repr(stderr_res))

## Connecting pipes
import tempfile
input_str ='''
I love you
You love him
You hates her
I hates him
'''
# No immediate deletion as 'cat' will use it
input_tmp_file = tempfile.NamedTemporaryFile(delete=False)
input_tmp_file.write(input_str.encode('utf-8'))
# close it as on Windows, it can not be opened a second time when it's already open
input_tmp_filename = input_tmp_file.name
input_tmp_file.close()
cat = subprocess.Popen(
    ['cat', input_tmp_filename ],
    ## in connected pipes, it's non-trivial to pass string as stdin
    # see https://stackoverflow.com/q/295459/2526378
    ## Let's avoid this arduous effort as suggested. I'm creating a temp file
    # solution.
    # stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
)

grep = subprocess.Popen(
    ['grep', 'love'],
    stdin = cat.stdout,
    stdout = subprocess.PIPE,
)

cut = subprocess.Popen(
    ['cut', '-d ', '-f', '3'],
    stdin = grep.stdout,
    stdout = subprocess.PIPE,
)

print('Connected Pipes (those who are being loved):')
res = cut.stdout
for line in cut.stdout:
    print( line.decode('utf-8').strip() )

import os
os.remove(input_tmp_filename)
