number = int(input())
ways = 0
temp = number

if temp%4 == 0:
    ways += 1
if temp%5 == 0:
    ways += 1

while temp>5:
    temp -= 5
    if temp%4 == 0:
        ways += 1

print(ways)
