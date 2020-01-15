# textwrap_example.py
sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

print(sample_text)

# textwrap_fill.py

import textwrap

print(textwrap.fill(sample_text, 50))

# dedent

dedented_text = textwrap.dedent(sample_text)
print(dedented_text)
# this would leave one whitespace at the beginning of the whitespace (converted
# from the blank line)
print(textwrap.fill(dedented_text, 50))
dedented_text = dedented_text.strip()
print(textwrap.fill(dedented_text, 50))

# combining everything above
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print( '%d Columns:' % width )
    print( textwrap.fill(dedented_text, width = width) )

# indent
dedented_text = textwrap.dedent(sample_text).strip()
dedented_text = textwrap.fill(dedented_text, 50)
dedented_text += '\n\nSecond Paragraph after a blank line.'
final = textwrap.indent(dedented_text, '> ')
print(final)

# let's say we want blank line to have indent mark as well
print('*************************************')
def should_indent(line):
    return True

final = textwrap.indent(dedented_text, '> ', predicate = should_indent)
print(final)

# Hanging indents
dedented_text = textwrap.dedent(sample_text).strip()
final = textwrap.fill(dedented_text,
                      initial_indent='',
                      subsequent_indent = '>' * 4,
                      width = 50,
                      )
print(final)

# Truncating long text
dedented_text = textwrap.dedent(sample_text).strip()
original = textwrap.fill(dedented_text, width = 50)

print('Original:\n%s' % original)
shortened_text = textwrap.shorten(sample_text, 100).strip()
print( 'Shortened:\n%s' % textwrap.fill(shortened_text, 50) )