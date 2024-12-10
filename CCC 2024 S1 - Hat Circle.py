circleList = [input() for i in range(int(input()))]

left = circleList[:len(circleList)//2]
right = circleList[len(circleList)//2:]

count = 0

for i,number in enumerate(left):
    if number == right[i]:
        count += 2

print(count)
