length = int(input())
a = input()
number = [] 
number = a.split(" ")
max = int(number[0])
min = int(number[0])
for i in range(length):
    if (int(number[i]) > int(max)):
        max = number[i]
    if (int(number[i]) < int(min)):
        min = number[i]
        
print(min, max)
