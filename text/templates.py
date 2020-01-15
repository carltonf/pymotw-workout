# TODO: string formats are very complex


# string_template.py
import string

values = { 'var': 'foo', 'var2': 'bar' }

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
Variable 2       : $var2
Escape           : $$
Variable in text : ${var2}iable
""")

print('TEMPLATE:', t.substitute(values))

# Below: string interpolations:

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
Variable 2        : %(var2)s
Escape            : %%
Variable in text  : %(var2)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable 2 in text: {var}iable
Variable          : {var2}
Escape            : {{}}
Variable in text  : {var2}iable
"""

print('FORMAT:', s.format(**values))

# limitation
nums = { 'num': 30, 'num2': 103 }
s = "Number: {num:04d}, Number 2: {num:05d}"
print( 'FORMAT:', s.format(**nums) )
# Template: No formatting options are available.
# s = string.Template( "Number: ${num:04d}, Number 2: ${num2:05d}" )
s = string.Template( "Number: ${num}, Number 2: ${num2}" )
print( 'TEMPLATE:', s.substitute(nums) )

# string_template_missing.py
# safe_substitute

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))

# string_template_advanced.py

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
  Delimiter  : %%
  Replaced   : %with_underscore
  Ignored    : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored':  'not replaced'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print( t.safe_substitute(d) )

t = string.Template('$var')
print( t.pattern )
print( t.pattern.pattern )

# completely change the pattern
class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

t = MyTemplate('''
{{{{
{{var}}
''')

print('MATCHES:', t.pattern.findall( t.template ))
print('SUBSTITUTED:', t.safe_substitute(var = 'replacement'))

# string constants

import inspect
def is_str(value):
    return isinstance(value, str)

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))