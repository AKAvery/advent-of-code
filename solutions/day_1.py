input = 'first.txt'
final = 0
with open(input, 'r') as f:
    original = f.readlines()

numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for lines in original:
    first = None
    last = None
    for index, char in enumerate(lines): 
        if char.isdigit() == True:
            last = char
    
        for i in range(6):
            if lines[index:index+i] in numbers:
                last = numbers[lines[index:index+i]]
        
    for index, char in enumerate(lines):
        if char.isdigit() == True:
            if first == None:
                first = char
                break
        
        for i in range(6):
            if first == None:
                if lines[index:index+i] in numbers:
                    first = numbers[lines[index:index+i]]
                    break

            
    if first is not None:
        single = first + last
        final += int(single)
        print(final)
