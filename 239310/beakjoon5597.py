number = list(range(1,31))
chk = []
for i in range(28):
    chk.append(int(input()))
sa = set(number)
sb = set(chk)
result = sa - sb
print(min(result))
print(max(result))

