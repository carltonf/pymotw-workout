# https://pymotw.com/3/string/index.html
import string

s = 'The   quick brown fox jumped over the lazy dog.'

print(s)
print( string.capwords(s)  )

# equivalent to
print(s)
rs = ''
for w in s.split():
    rs = ' '.join( [rs, w.capitalize()] )

print( rs.strip() )