cnt = int(input())
test = []
testFor = []
avg = []
overAvgPer = []

for i in range(cnt):
    test.append(input())

for i in range(cnt):
    testFor = test[i].split(" ")
    personCnt = int(testFor[0])
    sum =  0
    for j in range(1,personCnt+1):
        sum = sum + int(testFor[j])
    avg.append(sum / personCnt)

    overCnt = 0
    for k in range(1,len(testFor)):
        if(avg[i] < int(testFor[k])):
            overCnt = overCnt + 1
    overAvgPer.append(overCnt / personCnt * 100)
    
for i in overAvgPer:
    result = '%.3f' %round(i,3)
    print(f"{result}%")