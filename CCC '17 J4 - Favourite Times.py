timepass = int(input())
hourspass = timepass // 60
minutespass = timepass % 60
basetime = 1200
count = (hourspass//12)*31
hourspass = hourspass%12

for i in range(1,hourspass+1):
    for i in range(0,60):
        test = str(basetime+i)
        if int(test) > 999:
            if int(test[1])-int(test[0]) == int(test[2])-int(test[1]) == int(test[3])-int(test[2]):
                count += 1
        else:
            if int(test[1])-int(test[0]) == int(test[2])-int(test[1]):
                count += 1
    basetime += 100
    if basetime == 1300:
        basetime = 100

for i in range(1,minutespass+1):
    test = str(basetime+i)
    if int(test) > 999:
        if int(test[1])-int(test[0]) == int(test[2])-int(test[1]) == int(test[3])-int(test[2]):
            count+=1
    else:
        if int(test[1])-int(test[0]) == int(test[2])-int(test[1]):
            count+=1

print(count)
