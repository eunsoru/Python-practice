wordlist = input().lower().split()

trival = ['in','at','on','to','of','by','the','a','an']
wordlist = [i for i in wordlist if i not in trival]
wordlist[1] = wordlist[1][:3]

if wordlist[0] == 'bool':
    wordlist[0] = 'b'
elif wordlist[0] == 'int':
     wordlist[0] = 'i'
elif wordlist[0] == 'float':
     wordlist[0] = 'fp'
elif wordlist[0] == 'complex':
     wordlist[0] = 'cplx'
elif wordlist[0] == 'list':
     wordlist[0] = 'ls'

print('_'.join(wordlist))


