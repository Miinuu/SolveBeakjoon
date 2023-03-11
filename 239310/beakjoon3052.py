a = []
cnt = 0
rest = []
for i in range(10):
    a = int(input())
    rest.append(a % 42)
for i in range(len(rest)):
    j = i + 1
    if(j > 9):
        break
    while(rest[i] != rest[j]):
        if(j > 9):
            cnt = cnt +1
            break
        j = j+1
print(cnt)
