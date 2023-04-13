lang = 'Python'

print(lang.isupper()) #
print(lang.islower())
print(lang[0].isupper())
print(lang[1].islower())

print(lang.upper()) # 대문자로 바꿈
print(lang)
print(lang.lower()) # 소문자로 바꿈
print(lang)

name = ""
for i in range(len(lang)):
    if i % 2 == 0: # 
        name += lang[i].lower() # lang의 i번째를 소문자로 바꿈
    else: # 
        name += lang[i].upper() # lang
print(name)