import pygame



Board = [[0,0,3,0,2,0,6,0,0],
         [9,0,0,3,0,5,0,0,1],
         [0,0,1,8,0,6,4,0,0],
         [0,0,8,1,0,2,9,0,0],
         [7,0,0,0,0,0,0,0,8],
         [0,0,6,7,0,8,2,0,0],
         [0,0,2,6,0,9,5,0,0],
         [8,0,0,2,0,3,0,0,9],   
         [0,0,5,0,1,0,3,0,0]]

def valid(pos, num):

    for row in range(len(Board)):
        if (Board[pos[1]][row] == num and (pos[1], row) != pos) or (Board[row][pos[0]] == num and (row, pos[0]) != pos):
            return False

    # for 3x3 section 
    x = pos[0]//3
    y = pos[1]//3

    for row in range(y*3, y*3+3):
        for col in range(x*3, x*3+3):
            if Board[row][col] == num and (row,col) != pos:
                return False
    return True


def space():
    for row in range(len(Board)):
        for col in range(len(Board[0])):
            if Board[row][col] == 0:
                return (col, row)
    return False


def solve(num = None):
    emptyPos = space() 
    if not emptyPos:
        return True
    row,col = emptyPos[1], emptyPos[0]

    for num in range(1,10):
        if valid(emptyPos, num):
            Board[row][col] = num 
            if solve(num):
                return True
            Board[row][col] = 0
    return False

def print_board():
    for row in range(len(Board)):
        if row % 3 == 0 and row != 0:
            print("----------------------")
        for col in range(len(Board[0])):
            if col%3 == 0 and col != 0:
                print("| ", end="")
            print(Board[row][col], end=" ")
        print()

print_board()
print()
solve()
print_board()
