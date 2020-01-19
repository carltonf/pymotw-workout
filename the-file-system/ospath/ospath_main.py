import os.path

print('-------------- split, dirname, basename:')
PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

for p in PATHS:
    print('os.path.split:')
    print('{!r:>18}: {!r}'.format(p, os.path.split(p)))
    print('os.path.dirname:')
    print('{!r:>18}: {!r}'.format(p, os.path.dirname(p)))
    print('os.path.basename:')
    print('{!r:>18}: {!r}'.format(p, os.path.basename(p)))


# extension
print('-------------- splitext:')
PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

for p in PATHS:
    print( '{!r:>21}:{!r}'.format( p, os.path.splitext(p) ) )


print('-------------- commonprefix, commonpath:')

PATHS = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
for path in PATHS:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonprefix(PATHS))

print('> Also works for arbitrary lines, and thus does NOT respect path boundaries...')
LINES = [
    'this is just some plain text',
    'this is just some plain line',
    'this is just some plain string',
]
for line in LINES:
    print('LINE:', line)
print()
print(os.path.commonprefix(LINES))

print('> Try os.path.commonpath')
print( 'commonprefix:', os.path.commonpath(PATHS) )
print( 'commonpath:', os.path.commonpath(LINES) )