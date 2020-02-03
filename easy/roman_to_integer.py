import collections

roman = 'XXIV'
mapping = collections.OrderedDict([
    ('M', 1000),
    ('D', 500),
    ('C', 100),
    ('L', 50),
    ('X', 10),
    ('V', 5),
    ('I', 1),
    ('IV', 4),
    ('IX', 9),
    ('XL', 40),
    ('XC', 90),
    ('CD', 400),
    ('CM', 900)
])


sum = 0
i = 0
length = len(roman)
while i < length:
    ch = roman[i]
    if i < (length-1):
        if mapping.keys().index(ch) > mapping.keys().index(roman[i+1]):
            sum = sum + mapping.get(ch+roman[i+1])
            i = i + 2
        else:
            sum = sum + mapping.get(ch)
            i = i + 1
print(sum)
