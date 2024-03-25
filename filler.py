import pygame
import random

purple = pygame.Rect(200, 640, 50, 50)
red = pygame.Rect(250, 640, 50, 50)
green = pygame.Rect(300, 640, 50, 50)
blue = pygame.Rect(350, 640, 50, 50)

color_arr = ['purple', 'red', 'green', 'blue']
game_turn = 0
red_count = 0
purple_count = 0
green_count = 0
blue_count = 0

players_board = [[0, 0, 0, -1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 0]]


def set_color():
    global red_count, blue_count, green_count, purple_count
    color = color_arr[random.randint(0, 3)]

    if color == 'red' and red_count < 4:
        red_count += 1

        return pygame.Color(color)
    elif color == 'red' and red_count == 4:
        return set_color()

    if color == 'blue' and blue_count < 4:
        blue_count += 1

        return pygame.Color(color)
    elif color == 'blue' and blue_count == 4:
        return set_color()

    if color == 'green' and green_count < 4:
        green_count += 1

        return pygame.Color(color)
    elif color == 'green' and green_count == 4:
        return set_color()

    if color == 'purple' and purple_count < 4:
        purple_count += 1

        return pygame.Color(color)
    elif color == 'purple' and purple_count == 4:
        return set_color()


class Cell:
    def __init__(self):
        self.captured = False
        self.value = 0
        self.color = set_color()


def classify_board(board, players_board):
    for i in range(4):
        for j in range(4):
            if players_board[i][j] == 1:
                board[i][j].value = 1
                board[i][j].captured = True
            if players_board[i][j] == -1:
                board[i][j].value = -1
                board[i][j].captured = True


grid_size = 4
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]
classify_board(board, players_board)
pygame.init()
window = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()


def define_captures(player, color, i, j):
    if player == 1:
        for x in range(4):
            for y in range(4):
                if players_board[x][y] == 1:
                    board[x][y].color = pygame.Color(color)
    elif player == -1:
        for x in range(4):
            for y in range(4):
                if players_board[x][y] == -1:
                    board[x][y].color = pygame.Color(color)
    if i + 1 < 4 and board[i + 1][j].color == pygame.Color(color) and board[i + 1][j].captured == False:
        board[i + 1][j].value = player
        players_board[i + 1][j] = player
        print(players_board)
        define_captures(player, color, i + 1, j)
    if i - 1 >= 0 and board[i - 1][j].color == pygame.Color(color) and board[i - 1][j].captured == False:
        board[i - 1][j].value = player
        board[i - 1][j].captured = True
        players_board[i - 1][j] = player
        print(players_board)
        define_captures(player, color, i - 1, j)
    if j + 1 < 4 and board[i][j + 1].color == pygame.Color(color) and board[i][j + 1].captured == False:
        board[i][j + 1].value = player
        players_board[i][j + 1] = player
        print(players_board)
        define_captures(player, color, i, j + 1)
    if j - 1 >= 0 and board[i][j - 1].color == pygame.Color(color) and board[i][j - 1].captured == False:
        board[i][j - 1].value = player
        board[i][j - 1].captured = True
        players_board[i][j - 1] = player
        print(players_board)
        define_captures(player, color, i, j - 1)


run = True
while run:
    clock.tick(100)
    if game_turn % 2 == 0:
        pygame.display.set_caption('Player 1 turn')
    else:
        pygame.display.set_caption('Player 2 turn')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(4):
                for j in range(4):
                    piece = board[i][j]
                    if red.collidepoint(event.pos):
                        if game_turn % 2 == 0:
                            if piece.captured and piece.value == 1:
                                piece.color = pygame.Color('red')
                                piece.value = 1
                                define_captures(1, 'red', i, j)
                        else:
                            if piece.captured and piece.value == -1:
                                piece.color = pygame.Color('red')
                                piece.value = -1
                                define_captures(-1, 'red', i, j)
                    if blue.collidepoint(event.pos):
                        if game_turn % 2 == 0:
                            if piece.captured and piece.value == 1:
                                piece.color = pygame.Color('blue')
                                piece.value = 1
                                define_captures(1, 'blue', i, j)
                        else:
                            if piece.captured and piece.value == -1:
                                piece.color = pygame.Color('blue')
                                piece.value = -1
                                define_captures(-1, 'blue', i, j)
                    if green.collidepoint(event.pos):
                        if game_turn % 2 == 0:
                            if piece.captured and piece.value == 1:
                                piece.color = pygame.Color('green')
                                piece.value = 1
                                define_captures(1, 'green', i, j)
                        else:
                            if piece.captured and piece.value == -1:
                                piece.color = pygame.Color('green')
                                piece.value = -1
                                define_captures(-1, 'green', i, j)
                    if purple.collidepoint(event.pos):
                        if game_turn % 2 == 0:
                            if piece.captured and piece.value == 1:
                                piece.color = pygame.Color('purple')
                                piece.value = 1
                                define_captures(1, 'purple', i, j)
                        else:
                            if piece.captured and piece.value == -1:
                                piece.color = pygame.Color('purple')
                                piece.value = -1
                                define_captures(-1, 'purple', i, j)
            game_turn += 1
    window.fill(pygame.Color(40, 40, 40))
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.captured:
                pygame.draw.rect(window, cell.color, (ix * 150 + 1, iy * 150 + 1, 148, 148))
            else:
                pygame.draw.rect(window, cell.color, (ix * 150 + 1, iy * 150 + 1, 148, 148))

    pygame.draw.rect(window, [255, 0, 0], red)
    pygame.draw.rect(window, [0, 0, 255], blue)
    pygame.draw.rect(window, [0, 255, 0], green)
    pygame.draw.rect(window, [155, 0, 255], purple)

    pygame.display.flip()

pygame.quit()
exit()
