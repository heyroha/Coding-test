str = input()
result = []

for idx,i in enumerate(str):
    if i.isupper():
        result.append(i.lower())
    else:
        result.append(i.upper())
        
result = ''.join(result)
print(result)
