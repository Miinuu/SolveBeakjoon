test_num = int(input())
old_score = []
new_score = []
old_score = input().split(" ")
max = int(old_score[0])
for i in range(test_num):
    if( max < int(old_score[i])):
        max = int(old_score[i])
for i in range(test_num):
    new_score.append(int(old_score[i]) / max * 100)

result = sum(new_score) / test_num
print(result)


    