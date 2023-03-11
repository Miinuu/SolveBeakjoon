testcase = int(input())
result = []
strList = []
mulCnt = []
for i in range(testcase):
    case = list(input().split(" "))
    cnt = int(case[0])
    mulCnt.append(cnt)
    strList = list(case[1])
    result.append(strList)

k = 0
for i in result:
    for j in i:
        print(j*mulCnt[k],end="")
    print("")
    k += 1

