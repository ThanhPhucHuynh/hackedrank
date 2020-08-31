def displayPathtoPrincess(n,grid):

    
    for index, rowValue in enumerate(grid):
        if 'm' in rowValue:
           mario = [index, rowValue.index('m')]
        if 'p' in rowValue:
            princess = [index, rowValue.index('p')]
    
    #get relative position 
    positionY = mario[0] - princess[0]
    positionX = mario[1] - princess[1]


    solution = ""
    if positionY < 0 :
        solution+="DOWN\n"*abs(positionY)
    else:
         solution+="UP\n"*abs(positionY)
    if positionX < 0:
        solution+="RIGHT\n"*abs(positionX)
    else: solution+="LEFT\n"*abs(positionX)

    return solution
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
# m = 3
# grid = ['-m-', '---', '--p']

print(displayPathtoPrincess(m,grid))