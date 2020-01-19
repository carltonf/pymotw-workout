import os

if os.name == 'nt':
    print('Let this test be run on Unix system. Abort!')
    exit(-1)

print('----------- expand user')
for user in ['', 'vagrant', 'nosuchuser']:
    lookup = '~' + user
    print( '{:>12}: {}'.format(lookup, os.path.expanduser(lookup)) )


print('----------- expand environment var')

envars = [ 'HOME', 'NEWVAR', 'NOEXISTENT' ]
for v in envars:
    lookup = '$' + v
    os.environ['NEWVAR'] = 'new-value'
    print( '{!r:>16}: {!r}'.format(lookup, os.path.expandvars(lookup)) )