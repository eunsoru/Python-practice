def LeftToRight(i):
    if string[i+1] == '#':
        string[i+1] = original[i]
    
    elif string[i+1] not in vowels:
        string[i+1] = '*'

    string[i], string[i+1] = string[i+1], string[i]
    
    return ''.join(string)

def RightToLeft(i):
    if string[i] == '*':
        string[i] = original[i]
    
    elif string[i] in vowels:
        string[i] = '#'
            
    string[i], string[i+1] = string[i+1], string[i]

    return ''.join(string)

string = input()
print(string)
string = list(string)

vowels = list('aioueAIOUE')

original = []

if string[0] == '|':
    original = string[1:]
    for i in range(len(string)-1):  
        print(LeftToRight(i))
    for i in range(len(string)-2,-1,-1):
        print(RightToLeft(i))
else:
    original = string[0:-1]
    for i in range(len(string)-2,-1,-1):
        print(RightToLeft(i))
    for i in range(len(string)-1):  
        print(LeftToRight(i))