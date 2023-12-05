input = 'first.txt'
final = 0
with open(input, 'r') as f:
    original = f.readlines()
new = 0
for lines in original:
    first = None
    last = None
    for char in lines: 
        if char.isdigit() == True:
            last = char
    for char in lines:
        if char.isdigit() == True:
            first = char
            break
    if first is not None:
        single = first + last
        final += int(single)
        print(final)







