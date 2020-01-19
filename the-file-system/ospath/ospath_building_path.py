import os

print('------------ join')
PATHS = [
    ('one', 'two', 'three'),
    ('\\', 'one', 'two', 'three'),
    ('\\one', '\\two', '\\three'),
]

for parts in PATHS:
    print( '{!r:>30}:{!r}'.format(parts, os.path.join( *parts )) )