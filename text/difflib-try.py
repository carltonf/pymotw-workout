# do not name this file as `difflib` as it confuses python interpreter with the
# standard `difflib`.


text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor.  In nec mauris eget magna consequat
convalis. Nam sed sem vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
tristique enim. Donec quis lectus a justo imperdiet tempus."""

text1_lines = text1.splitlines()
# print(text1_lines)

text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar, porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor. In nec mauris eget magna consequat
convalis. Nam cras vitae mi vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Duis vulputate tristique enim. Donec quis lectus a
justo imperdiet tempus.  Suspendisse eu lectus. In nunc."""

text2_lines = text2.splitlines()
# print(text2_lines)

# DON'T name your file as std modules
import difflib
differ = difflib.Differ()
diff = differ.compare(text1_lines, text2_lines)
# '\n'.join to convert generator object (diff) to string and also avoids
# auto-inserted whitespace before diff string
print('\n'.join(diff))

# other output formats

diff = difflib.unified_diff(
    text1_lines, text2_lines,
    # lineterm is the ending characters for control lines, by default it's a
    # newline.
    lineterm='',
)
print('\n'.join(diff))

diff = difflib.context_diff(
    text1_lines, text2_lines,
    lineterm = "",
    # default context line number is 3
    n = 2
)
print('\n'.join(diff))


# Junk Data

from difflib import SequenceMatcher

def show_results(match):
    print('  a       = {}'.format(match.a))
    print('  b       = {}'.format(match.b))
    print('  size    = {}'.format(match.size))
    i, j, k = match
    print('  A[a:a+size] = {!r}'.format(A[i:i+k]))
    print('  B[a:a+size] = {!r}'.format(B[j:j+k]))

A = " abcd"
B = "abcd abcd"

print('A = {!r}'.format(A))
print('B = {!r}'.format(B))

print('\nWithout junk detection:')
s1 = SequenceMatcher(None, A, B)
match1 = s1.find_longest_match(0, len(A), 0, len(B))
show_results(match1)

import re
print('\nTreat spaces as junk:')
s2 = SequenceMatcher(lambda x: re.match('\s+', x), A, B)
match2 = s2.find_longest_match(0, len(A), 0, len(B))
show_results(match2)

# Comparing arbitrary types

s1 = [1, 2, 3, 5, 6, 4]
s2 = [2, 3, 5, 4, 6, 1]

print('Original s1 and s2:')
print('s1 =', s1)
print('s2 =', s2)
print()

matcher = difflib.SequenceMatcher(None, s1, s2)

# ops are done in reversed order to keep indexes valid as changes are made in
# place.
for op, i1, i2, j1, j2 in reversed( matcher.get_opcodes() ):
    if op == 'delete':
        print('Remove {} from s1[{}:{}]'.format(
            s1[i1:i2], i1, i2,
        ))
        print('  Before s1=', s1)
        del s1[i1:i2]
        print('  After s1=', s1)
    elif op == 'insert':
        print('Insert {} from s2[{}:{}] to s1[{}:{}]'.format(
            s2[j1:j2], j1, j2, i1, i2,
        ))
        print('  Before s1=', s1)
        s1[i1:i2] = s2[j1:j2]
        print('  After s1=', s1)
    elif op == 'equal':
        print('s1[{}:{}] and s2[{}:{}] are the same.'.format(
            i1, i2, j1, j2,
        ))
    elif op == 'replace':
        print('Replace {} in s1[{}:{}] with {} from s2[{}:{}]'.format(
            s1[i1:i2], i1, i2, s2[j1:j2], j1, j2,
        ))
        print('  Before s1=', s1)
        s1[i1:i2] = s2[j1:j2]
        print('  After s1=', s1)

print('s1 == s2', s1 == s2)