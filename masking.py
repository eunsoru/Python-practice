a, b = map(str, input().split())
c = input()
d = list(c)

if a == 'v':
    for i in range(len(d)):
        if d[i] in ['a', 'o', 'i', 'e', 'u']:
            d[i] = b
else:
    for i in range(len(d)):
        if d[i] not in ['a', 'o', 'i', 'e', 'u', ' ']:
            d[i] = b

e = ''.join(d)

print(e)