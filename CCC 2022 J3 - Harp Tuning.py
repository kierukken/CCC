input = list(input())
list = []
numlist =[]
tempnumlist = []
templist = []
lastdigit = False
input.append("")
pos = False

for x in input:
    if x != "-" and x != "+" and x.isdigit() == False:
        templist.append(x)
    elif x == "-" or x == "+":
        if x == "-":
            pos = True
        list.append(templist)
        templist = []
    if x.isdigit() == True:
        if pos == True:
            tempnumlist.append(int(x)*-1)
            pos = False
            lastdigit = True
        else:
            tempnumlist.append(int(x))
            lastdigit = True
    else:
        if lastdigit == True:
            numlist.append(tempnumlist)
            tempnumlist = []
            lastdigit = False
list = ["".join(x) for x in list]
numlist = [int(''.join(map(str, x))) for x in numlist]

for x in range(len(list)):
    if numlist[x] > 0:
        tuning = "tighten"
    if numlist[x] < 0:
        tuning = "loosen"
    print(f'{list[x]} {tuning} {abs(numlist[x])}')
