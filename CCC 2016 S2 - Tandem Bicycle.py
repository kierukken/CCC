question = int(input())
citizens = int(input())
dmoj, peg = [], []
dmoj, peg = map(int, input().split()), map(int, input().split())
dmoj, peg = sorted(dmoj), sorted(peg)
speed = 0


if question == 1:
    for i in range(citizens):
        speed += max(dmoj[i],peg[i])

if question == 2:
    for i in range(citizens):
        speed += max(dmoj[i],peg[citizens-1-i])
print(speed)
