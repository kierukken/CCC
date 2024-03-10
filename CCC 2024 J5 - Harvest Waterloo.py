rows = int(input())
columns = int(input())
field = []
count = 0
booleanField = []
for i in range(rows):
    row_input = input("".format(i+1))
    field.append([char for char in row_input])
    booleanField.append([False for char in row_input])
startY = int(input())
startX = int(input())
def flood_fill(x, y):
    global count, field, booleanField
    if 0 > x or x > rows-1 or 0 > y or y > columns-1:
        return
    if booleanField[x][y] is True or field[x][y] == "*":
        return
    if field[x][y] == "S":
        count += 1
    elif field[x][y] == "M":
        count += 5
    elif field[x][y] == "L":
        count += 10

    booleanField[x][y] = True
    array = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for dx, dy in array:
        flood_fill(dx, dy)

flood_fill(startY, startX)
print(count)
