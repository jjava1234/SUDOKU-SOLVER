import pygame

win = pygame.display.set_mode((450,500))
win.fill((255,255,255))
pygame.display.set_caption('Sudoku Solver')

Board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

num_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, 
            pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
num_pads = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, 
            pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
def main():
    selected = None
    run = True
    draw_grid()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]//50 
                y = (pos[1]-50)//50 
                selected = (x, y)
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        solve()
                    elif event.key == pygame.K_F2:
                        for row in Board:
                            for col in row:
                                Board[row][col] = 0
                    elif event.key == pygame.K_F3:
                        pygame.quit()
                    elif selected:
                        if event.key in num_keys or event.key in num_pads: 
                            x, y = selected[0], selected[1]
                            selected = None
                            if event.key == pygame.K_KP0:
                                Board[y][x] = 0                         
                            elif event.key in num_keys:
                                Board[y][x] = event.key - 48
                            else:
                                Board[y][x] = event.key - 1073741912

                        draw_box()
        pygame.display.update()


def draw_grid():
    for row in range(len(Board)):
        for col in range(len(Board[0])):   
            if row % 3 == 0 and col % 3 == 0:
                pygame.draw.rect(win, (0,0,0), (col*50, row*50+50, 150, 150), 3)
            pygame.draw.rect(win, (0,0,0), (col*50, row*50+50, 50, 50), 1)
    draw_box()

def draw_box():
    pygame.font.init()
    font = pygame.font.SysFont('Calibri', 13)
    img = font.render("F1 TO SOLVE      F2 TO RESET        F3 TO EXIT", False, (0,0,0))
    win.blit(img, (62, 25))

    font = pygame.font.SysFont('Calibri', 20)
    img = font.render("PLEASE ENTER A VALID SUDOKU LAYOUT", False, (0,0,0))
    win.blit(img, (225 - img.get_width()//2, 0))
    for row in range(len(Board)):
        for col in range(len(Board[0])):
            if num := Board[row][col]:
                pygame.draw.rect(win,(255,255,255), (col*50+15, row*50+68, 20, 20))
                img = font.render(f"{num}", False, (0,0,0))
                win.blit(img, (col*50+20, row*50+70))


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
        print(Board)
        draw_box()        
        return True 
    row,col = emptyPos[1], emptyPos[0]

    for num in range(1,10):
        print(Board)
        if valid(emptyPos, num):
            Board[row][col] = num 
            if solve(num):
                return True
            Board[row][col] = 0
    return False

main()
