import os

print('----------- normalize path')

PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))


print('----------- absolute path')
print('Current Working directory:', os.getcwd())
PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in PATHS:
    print( '{!r:>20}:{!r}'.format(path, os.path.abspath(path)) )