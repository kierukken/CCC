import sys
sys.setrecursionlimit(1000000)

height = int(input())
length = int(input())

grid = [list(input()) for i in range(height)]

startingy = int(input())
startingx = int(input())

total = 0

def fill(x,y, grid):
    global total, length, height
    if grid[y][x] == 'S':
        total+= 1
    elif grid[y][x] == 'M':
        total += 5
    elif grid[y][x] == 'L':
        total += 10
    grid[y][x] = '*'
    if x+1 < length and grid[y][x+1] != '*':
        fill(x+1,y, grid)
    if x-1 >= 0 and grid[y][x-1] != '*':
        fill(x-1,y, grid)
    if y+1 < height and grid[y+1][x] != '*':
        fill(x,y+1, grid)
    if y-1 >= 0 and grid[y-1][x] != '*':
        fill(x,y-1, grid)
    return 0
fill(startingx, startingy, grid)
print(total)
