c = 'abcdefghijklm'
i1 = 0
tmp = list(c)
for i, x in enumerate(c):
    i1 = i + 2
    if i1 % 3 == 1:
        tmp[i] = x.upper()
    else:
        tmp[i] = x
result = ''.join(map(str, tmp))
print(result)
