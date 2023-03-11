test_num = int(input())
test = []
testFor = []
scoreList = list(0 for i in range(test_num))
for i in range(test_num):
    test.append(input())
for i in range(test_num):
    testFor = list(test[i])
    score = 0
    for j in range(len(testFor)):
        if(testFor[j] == 'O'):
            score = score + 1
            scoreList[i] = scoreList[i] + score
        elif(testFor[j] == 'X'):
            score = 0
    print(scoreList[i])