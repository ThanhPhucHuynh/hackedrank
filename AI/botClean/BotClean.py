#!/usr/bin/python

# Head ends here

dirts = []
finished = False
selected = -1




def find_all_dirts(board):
    n = len(board) #get cel
    m = len(board[0]) #get row
    
    for i in range(n):
        for y in range(m):
            if board[i][y] == 'd':
                dirts.append((i,y))
    global finished
    finished = True

def getMin(a,b):
    return a if a<b else b

def find_dirts(posr,posc):
    nim_dirts = 99999
    # index = -1
    for i in range(len(dirts)):
        x,y = dirts[i]
        x_value = abs(x-posr)
        y_value = abs(y-posc)
        line_value = x_value + y_value
        # print(line_value,nim_dirts,line_value<nim_dirts,i)
        if line_value < nim_dirts:
            nim_dirts = line_value
            index_choose = i

           # nim_dirts = getMin(line_value,nim_dirts)
    # print(index_choose)
    global selected
    selected = index_choose

def next_move(posr, posc, board):
    global selected
    global finished

    if finished == False :
        find_all_dirts(board)
    if selected == -1:
        find_dirts(posr,posc)
    
    dirt_x, dirt_y = dirts[selected]

    if posr == dirt_x and posc == dirt_y:
        print("CLEAN")
        dirts.pop(selected)
        selected = -1
    elif dirt_x > posr:
        print("DOWN")
    elif posr > dirt_x:
        print("UP")
    elif posc > dirt_y:
        print ("LEFT")
    elif dirt_y > posc:
        print("RIGHT")



if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(5)]
    board = [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
    pos   = [0,0]
    next_move(pos[0], pos[1], board)