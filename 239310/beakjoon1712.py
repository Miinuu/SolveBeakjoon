money = input().split(" ")
fixedOut = int(money[0])
flexOut = int(money[1])
price = int(money[2])
if(flexOut >= price):
    print("-1")
else:
    print(int(fixedOut / (price - flexOut) + 1))