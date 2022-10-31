import numpy as np
import pygame
import sys
from constant import WIDTH, HEIGHT, BG_COLOR, BOARD_ROWS, SQUARE_CENTER, YELLOW, BOARD_COLS, SQUARE_SIZE, \
    CIRCLE_COLOR_1, CIRCLE_RADIUS, CIRCLE_WIDTH, CIRCLE_COLOR_2, CIRCLE_COLOR_AVAILABLE, CIRCLE_COLOR_1_MOVE, \
    CIRCLE_COLOR_2_MOVE, LINE_WIDTH, LINE_COLOR, WIN_LINE_WIDTH, PLAYER_1_SCORE, PLAYER_2_SCORE, CURENT_PIECES, ROUND_START_PLAYER
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
screen.fill(BG_COLOR)
board = np.zeros((BOARD_ROWS, BOARD_COLS))
font_score = pygame.font.Font('freesansbold.ttf', 36)
font_name = pygame.font.Font('freesansbold.ttf', 15)
def draw_license():
    text = font_name.render("Created by Elis Bushaj", True, YELLOW)
    screen.blit(text, (HEIGHT - (SQUARE_CENTER + SQUARE_SIZE // 2), WIDTH - (SQUARE_CENTER//2)))
def score(p1, p2):
    text = font_score.render(f"Score: {p1} - {p2}", True, YELLOW)
    screen.blit(text, (SQUARE_CENTER//3, SQUARE_CENTER//3))
def draw_info():
    text_1 = font_name.render("Press 'R' to Restart,", True, YELLOW)
    text_2 = font_name.render("Press 'Return' to Continue", True, YELLOW)
    screen.blit(text_1, (SQUARE_CENTER // 2, WIDTH - SQUARE_CENTER // 2))
    screen.blit(text_2, (SQUARE_CENTER // 2, WIDTH - (SQUARE_CENTER // 2) + SQUARE_CENTER // 6))
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR_1, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR_2, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 3:
                pygame.draw.circle(screen, CIRCLE_COLOR_AVAILABLE, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS // 2,
                                   CIRCLE_WIDTH // 2)
            elif board[row][col] == 5:
                pygame.draw.circle(screen, CIRCLE_COLOR_1_MOVE, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 6:
                pygame.draw.circle(screen, CIRCLE_COLOR_2_MOVE, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
def check_player(row, col, player):
    return board[row][col] == player
def go_back(player):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 3:
                board[row][col] = 0

            elif board[row][col] == 5:
                board[row][col] = player

            elif board[row][col] == 6:
                board[row][col] = player
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    draw_info()
    score(PLAYER_1_SCORE, PLAYER_2_SCORE)
def remove_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 3:
                board[row][col] = 0

            elif board[row][col] == 5:
                board[row][col] = 0

            elif board[row][col] == 6:
                board[row][col] = 0
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    draw_info()
    score(PLAYER_1_SCORE, PLAYER_2_SCORE)
def move_piece(row, col, player):
    board[row][col] = player
    remove_figures()
def piece_ready_to_move(row, col):
    if board[row][col] == 1:
        board[row][col] = 5
    elif board[row][col] == 2:
        board[row][col] = 6
def mark_square(row, col, player):
    board[row][col] = player
def available_square_to_move(row, col):
    if row == 0 and col == 0:
        if board[0][1] == 0:
            board[0][1] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[1][0] == 0:
            board[1][0] = 3
    if row == 0 and col == 1:
        if board[0][0] == 0:
            board[0][0] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[0][2] == 0:
            board[0][2] = 3
    if row == 0 and col == 2:
        if board[0][1] == 0:
            board[0][1] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[1][2] == 0:
            board[1][2] = 3
    if row == 1 and col == 0:
        if board[0][0] == 0:
            board[0][0] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[2][0] == 0:
            board[2][0] = 3
    if row == 1 and col == 1:
        if board[0][0] == 0:
            board[0][0] = 3
        if board[0][1] == 0:
            board[0][1] = 3
        if board[0][2] == 0:
            board[0][2] = 3
        if board[1][0] == 0:
            board[1][0] = 3
        if board[1][2] == 0:
            board[1][2] = 3
        if board[2][0] == 0:
            board[2][0] = 3
        if board[2][1] == 0:
            board[2][1] = 3
        if board[2][2] == 0:
            board[2][2] = 3
    if row == 1 and col == 2:
        if board[0][2] == 0:
            board[0][2] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[2][2] == 0:
            board[2][2] = 3
    if row == 2 and col == 0:
        if board[1][0] == 0:
            board[1][0] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[2][1] == 0:
            board[2][1] = 3
    if row == 2 and col == 1:
        if board[2][0] == 0:
            board[2][0] = 3
        if board[1][1] == 0:
            board[1][1] = 3
        if board[2][2] == 0:
            board[2][2] = 3
    if row == 2 and col == 2:
        if board[1][2] == 0:
            board[1][2] = 3

        if board[1][1] == 0:
            board[1][1] = 3

        if board[2][1] == 0:
            board[2][1] = 3
def available_move(row, col):
    return board[row][col] == 3
def available_square(row, col):
    return board[row][col] == 0
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_CENTER, SQUARE_CENTER),
                     (SQUARE_SIZE * 3 - SQUARE_CENTER, SQUARE_SIZE * 3 - SQUARE_CENTER), LINE_WIDTH + 2)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * 3 - SQUARE_CENTER, SQUARE_CENTER),
                     (SQUARE_CENTER, SQUARE_SIZE * 3 - SQUARE_CENTER), LINE_WIDTH + 2)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * 2 - SQUARE_CENTER, SQUARE_CENTER),
                     (SQUARE_SIZE * 2 - SQUARE_CENTER, SQUARE_SIZE * 3 - SQUARE_CENTER), LINE_WIDTH - 2)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_CENTER, SQUARE_SIZE * 2 - SQUARE_CENTER),
                     (SQUARE_SIZE * 3 - SQUARE_CENTER, SQUARE_SIZE * 2 - SQUARE_CENTER), LINE_WIDTH - 2)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(SQUARE_CENTER, SQUARE_CENTER, WIDTH - (SQUARE_CENTER * 2),
                                                     WIDTH - (SQUARE_CENTER * 2)), LINE_WIDTH)
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False
def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR_1
    elif player == 2:
        color = CIRCLE_COLOR_2
    pygame.draw.line(screen, color, (posX, SQUARE_CENTER), (posX, HEIGHT - SQUARE_CENTER), LINE_WIDTH)
def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR_1
    elif player == 2:
        color = CIRCLE_COLOR_2
    pygame.draw.line(screen, color, (SQUARE_CENTER, posY), (WIDTH - SQUARE_CENTER, posY), WIN_LINE_WIDTH)
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR_1
    elif player == 2:
        color = CIRCLE_COLOR_2
    pygame.draw.line(screen, color, (SQUARE_CENTER, HEIGHT - SQUARE_CENTER), (WIDTH - SQUARE_CENTER, SQUARE_CENTER),
                     WIN_LINE_WIDTH)
def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR_1
    elif player == 2:
        color = CIRCLE_COLOR_2
    pygame.draw.line(screen, color, (SQUARE_CENTER, SQUARE_CENTER), (WIDTH - SQUARE_CENTER, HEIGHT - SQUARE_CENTER),
                     WIN_LINE_WIDTH)
def restart():
    screen.fill(BG_COLOR)
    score(PLAYER_1_SCORE, PLAYER_2_SCORE)
    draw_info()
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
draw_lines()
score(PLAYER_1_SCORE, PLAYER_2_SCORE)
draw_info()
draw_license()
player = None
game_over = False
while True:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if CURENT_PIECES < 6:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)
                    if available_square(clicked_row, clicked_col):
                        CURENT_PIECES = CURENT_PIECES + 1
                        if CURENT_PIECES == 1:
                            mark_square(clicked_row, clicked_col, ROUND_START_PLAYER)
                            if check_win(player):
                                game_over = True
                            else:
                                player = ROUND_START_PLAYER % 2 + 1
                            PIECE_CLICK_STATE = False
                            draw_figures()
                        else:
                            mark_square(clicked_row, clicked_col, player)
                            if check_win(player):
                                game_over = True
                            else:
                                player = player % 2 + 1
                            PIECE_CLICK_STATE = False
                            draw_figures()
            else:
                if PIECE_CLICK_STATE:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not game_over:
                        go_back(player)
                        PIECE_CLICK_STATE = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                        mouseX = event.pos[0]  # x
                        mouseY = event.pos[1]  # y
                        clicked_row = int(mouseY // SQUARE_SIZE)
                        clicked_col = int(mouseX // SQUARE_SIZE)
                        if available_move(clicked_row, clicked_col):
                            move_piece(clicked_row, clicked_col, player)
                            if check_win(player):
                                game_over = True
                            else:
                                player = player % 2 + 1
                            PIECE_CLICK_STATE = False
                            draw_figures()
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        clicked_row = int(mouseY // SQUARE_SIZE)
                        clicked_col = int(mouseX // SQUARE_SIZE)
                        if check_player(clicked_row, clicked_col, player):
                            available_square_to_move(clicked_row, clicked_col)
                            piece_ready_to_move(clicked_row, clicked_col)
                            PIECE_CLICK_STATE = True
                            draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    CURENT_PIECES = 0
                    PLAYER_1_SCORE = 0
                    PLAYER_2_SCORE = 0
                    restart()
                    game_over = False
        pygame.display.update()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    CURENT_PIECES = 0
                    PLAYER_1_SCORE = 0
                    PLAYER_2_SCORE = 0
                    restart()
                    game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    CURENT_PIECES = 0
                    if player == 1:
                        ROUND_START_PLAYER = 2
                        PLAYER_1_SCORE = PLAYER_1_SCORE + 1
                    elif player == 2:
                        ROUND_START_PLAYER = 1
                        PLAYER_2_SCORE = PLAYER_2_SCORE + 1
                    restart()
                    game_over = False