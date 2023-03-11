a = input()
metrics = a.split(" ")

total = int(metrics[0])
cutline = int(metrics[1])

b = input()
number = b.split(" ")
result = []
for i in range(total):
    if (int(number[i]) < cutline):
        result.append(number[i])
for i in result:
    print(i, end=' ')
