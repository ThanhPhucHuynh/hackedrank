import math
import json
import os

def update_board(board):
    if os.path.isfile("board"):
        old_board = json.load(open("board"))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "o":
                    board[i][j] = old_board[i][j]
    json.dump(board, open("board", "w"))


dirts = []
finished = False
selected = -1



def find_all_dirts(board):
    n = len(board) #get cel
    m = len(board[0]) #get row
    for i in range(n):
        for y in range(m):
            if board[i][y] == 'o': dirts.append((i,y))
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
        line_value =math.sqrt(x_value**2 + y_value**2)
        # print(line_value,nim_dirts,line_value<nim_dirts,i)
        if line_value < nim_dirts:
            nim_dirts = line_value
            index_choose = i

           # nim_dirts = getMin(line_value,nim_dirts)
    # print(index_choose)
    global selected
    selected = index_choose


def next_move(posx, posy, board):
    global selected
    global finished

    if finished == False :
        find_all_dirts( board)
    if selected == -1:
        find_dirts(posx, posy)

    # print(dirts)
    # print(board[0][1])
    dirt_x, dirt_y = dirts[selected]

    if posx == dirt_x and posy == dirt_y:
        print("CLEAN")
        dirts.pop(selected)
        selected = -1
    elif dirt_x > posx:
        print("DOWN")
    elif posx > dirt_x:
        print("UP")
    elif posy > dirt_y:
        print ("LEFT")
    elif dirt_y > posy:
        print("RIGHT")

    print(posx, posy, board)

if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # dim = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(dim[0])]
    board = [['b', 'd', 'o', 'o', 'o'], ['-', 'd', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
    update_board(board)
    next_move(0, 0, [['b', 'd', 'o', 'o', 'o'], ['-', 'd', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']])

    

    # 0 0 5 5 [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]