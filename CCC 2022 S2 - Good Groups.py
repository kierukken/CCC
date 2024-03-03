constraints = int(input())
samegroup = []
difgroup = []
dict = {}
violations = 0

if constraints > 0:
    for i in range(constraints):
        groups = input().split()
        samegroup.append(groups)

constraints = int(input())
if constraints > 0:
    for i in range(constraints):
        groups = input().split()
        difgroup.append(groups)

constraints = int(input())
for i in range(constraints):
    tri = input().split()
    for j in range(3):
        dict[tri[j]] = i

for x in range(len(samegroup)):
    p1 = dict[samegroup[x][0]]
    p2 = dict[samegroup[x][1]]
    if p1!=p2:
        violations+=1

for x in range(len(difgroup)):
    p1 = dict[difgroup[x][0]]
    p2 = dict[difgroup[x][1]]
    if p1 == p2:
        violations += 1

print(violations)
