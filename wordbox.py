word = input()
wordlist = list(word)

print(word)

for i in range(1,len(word)-1):
	print(word[i]+" "*(len(word)-2)+word[-(i+1)])

wordlist.reverse()
print(''.join(wordlist))
