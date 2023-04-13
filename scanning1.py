string = input()
stringList = list(string)
stringList2 = []

def rstar(x): 
    if x[i-1] not in ['a', 'o', 'i', 'e', 'u','A','O','I','E','U']:
        x[i-1] = '*'
            
def lstar(x):
    if -i != 0 and x[-i] in ['a', 'o', 'i', 'e', 'u','A','O','I','E','U']:
        x[-i] = '#'
    elif -i == 0 and x[-i] in ['a', 'o', 'i', 'e', 'u','A','O','I','E','U']:
        x[-1] = '#'




for i in range(len(stringList)):
    if i == len(stringList):
        break

    if i != 0 and i != len(stringList):
        stringList[i], stringList[i-1] = stringList[i-1],stringList[i]
        rstar(stringList)
    result = ''.join(stringList)
    print(result)

for i in range(len(stringList)):
    if i == 0:
        continue

    if i !=0 and i!= len(stringList):
        stringList[-i], stringList[-i-1] = stringList[-i-1],stringList[-i]
        
        lstar(stringList)
    result = ''.join(stringList)
    print(result)
    
    

