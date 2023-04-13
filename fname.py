word= input()
wordlist = word.split()

vowels = 'aioeu'
extword = ['a','an','the']

wordlist = [i for i in wordlist if i not in extword]

first = ''
for c in wordlist[0]:
    if c.lower() not in vowels: 
        first += c.lower()

for it in wordlist[1:]:
    first += it[0].upper() + it[1:].lower()

print(first)










