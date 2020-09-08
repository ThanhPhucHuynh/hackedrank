def nextMove(n,r,c,grid):

    for index, rowValue in enumerate(grid):
        if 'p' in rowValue:
            princess = [index, rowValue.index('p')]
    mario=[r,c]
    positionY = mario[0] - princess[0]
    positionX = mario[1] - princess[1]

    solution = ""

    if positionY ==0:
        if positionX < 0:
            solution="RIGHT"
        else: solution="LEFT"
    elif positionY < 0 :
        solution="DOWN"
    else:
        solution="UP"
    return solution


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

# n = 5
# r = 2
# c = 3
# grid = ['-----', 'm----', '-----', '-----', '-p---']

print(nextMove(n,r,c,grid))