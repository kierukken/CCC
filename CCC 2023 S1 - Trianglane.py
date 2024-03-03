colomns = int(input())
tape = 0
firstrow, secoundrow = input().split(), input().split()

array = firstrow + secoundrow

for x in array:
    if "1" in x:
        tape += 3

for x in range(0,colomns,2):
    if firstrow[x] == secoundrow[x] and firstrow[x] != "0":
        tape -= 2

for x in range(0, colomns-1):
    if firstrow[0+x] == "1" and firstrow[1+x] == "1":
        tape -= 2
    if secoundrow[0+x] == "1" and secoundrow[1+x] == "1":
        tape -= 2

print(tape)
