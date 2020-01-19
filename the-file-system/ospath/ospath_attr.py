import os

if os.name == 'nt':
    print('To make path normalization easier, only tested in Linux. Abort.')
    exit(-1)

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './broken_link',
]

for file in FILENAMES:
    print('File?             : {!r}'.format(file))
    print('Is Absolute Path? : {!r}'.format(os.path.isabs(file)))
    print('Is File?          : {!r}'.format(os.path.isfile(file)))
    print('Is Directory?     : {!r}'.format(os.path.isdir(file)))
    print('Is Link?          : {!r}'.format(os.path.islink(file)))
    print('Is MountPoint?    : {!r}'.format(os.path.ismount(file)))
    print('Exists?           : {!r}'.format(os.path.exists(file)))
    print('Link Exists?      : {!r}'.format(os.path.lexists(file)))
    print()
