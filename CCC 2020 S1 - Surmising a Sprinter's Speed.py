observations = int(input())
dict = {}
array = []
for i in range(observations):
    time,dist = list(map(int,input().split()))
    dict[time] = dist

keys = sorted(dict.keys())

for x in range(0,len(dict.keys())-1):
    atime = keys[x+1]-keys[x]
    adist = dict[keys[x+1]] - dict[keys[x]]
    array.append(abs(float(adist/atime)))

print(max(array))
