import pygame

red = pygame.Rect(275, 640, 50, 50)
blue = pygame.Rect(475, 640, 50, 50)
green = pygame.Rect(425, 640, 50, 50)


class Cell:
    def __init__(self):
        self.clicked = False


grid_size = 4
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]

pygame.init()
window = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                row = event.pos[1] // 150
                col = event.pos[0] // 150
                if row < 4 and col < 4:
                    board[row][col].clicked = True
            if red.collidepoint(event.pos):
                for i in range(4):
                    for j in range(4):
                        board[i][j] .clicked = True
            if blue.collidepoint(event.pos):
                for i in range(4):
                    for j in range(4):
                        board[i][j].clicked = False

    window.fill(pygame.Color('white'))
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            color = (155, 0, 0) if cell.clicked else (0, 0, 155)
            pygame.draw.rect(window, color, (ix * 150 + 1, iy * 150 + 1, 148, 148))

    pygame.draw.rect(window, [255, 0, 0], red)
    pygame.draw.rect(window, [0, 0, 255], blue)
    pygame.draw.rect(window, [0, 255, 0], green)

    pygame.display.flip()

pygame.quit()
exit()
