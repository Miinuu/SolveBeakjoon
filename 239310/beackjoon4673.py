def isSelfNumber(number):
    result = 0
    num_list= list(map(int, str(number)))
    result = number + sum(num_list)
    return result

number = list(range(1,10001))
notSelfNumberList = []
selfNumberList = []

for i in range(len(number)):
    notSelfNumberList.append(isSelfNumber(number[i]))


selfNumberList = set(number) - set(notSelfNumberList)

for i in sorted(selfNumberList):
    print(i)