# Convert a list of pages (written down by hand) to segments of ranges of pages
# recognized by printer dialog (in Windows).

# range_array = [ 33,  34, 37, 38, 41, 42, 48, 49, 50, 53, 56, 58, 63, 64, 65,
# 66, 67, 71, 73, 74, 77, 78, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94,
# 96, 98, 99, 100, 101, 102, 104, 106, 107, 108, 112, 116, 118, 119, 120, 121,
# 122, 123, 126, 127, 128, 134, 136, 137, 138, 139, 140, 146, 147, 149, 150,
# 152, 155, 156, 159, 161, 162, 164, ]
range_array = [161,162,164, 168, 169, 170, 173, 176,
177, 179, 182, 184, 195, 196, 198,
200, 201 ]
range_str = ''

# Constants:
# - At the start of a subrange, i and j are always equal
# - At any stage, j >= i
i = j = -2 # in case j + 1 would be 0, valid page num. in some case
for ip, p in enumerate(range_array):
    # next page
    if p == j + 1:
        j = p
        if ip == len(range_array) - 1:
            range_str += '%d-%d' % (i, j)
        continue
    # page skipped, new subrange
    elif p > j+1:
        if j != i:
            range_str += '%d-%d,' % (i, j)
        else:
            # NOT initial
            if i >= 0:
                range_str += '%d,' % i

        i = j = p
        if ip == len(range_array) - 1:
            range_str += '%d' % i
        continue

print(range_array)
print(range_str)
print('---------------------------------------------')

# NOTE: there will be a trailing comma at the last line
for i, r in enumerate( range_str.split(',') ):
    print(r, end='')
    if (i+1) % 5 == 0:
        print()
    else:
        print(',', end='')