cnt = int(input())
number = []
number_input = input()

number = number_input.split(" ")
isRight = 0
check = int(input())
for i in range(cnt):
    if(check == int(number[i])):
        isRight = isRight + 1
print(isRight)
    