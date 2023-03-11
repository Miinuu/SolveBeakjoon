number = [] 
for i in range(9):
    a = int(input())
    number.append(a)
max = number[0]
check = 0
for i in range(len(number)):
    if (int(number[i]) > int(max)):
        max = number[i]
    if (int(number[i]) == int(max)):
        check = i+1

print(max)
print(check)
