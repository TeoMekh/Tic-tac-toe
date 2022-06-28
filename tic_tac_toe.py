import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count('0')
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
        if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return sign
        if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
            return sign
    if zeroes == 0:
        return 'Draw'
    return False


pygame.init()
size_block = 100
border = 5
width = height = size_block * 3 + border * 4
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic tac toe")
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
query = 0
game_over = False

mas = [['0'] * 3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + border)
            row = y_mouse // (size_block + border)
            if mas[row][col] == '0':
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [['0'] * 3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * border
                y = row * size_block + (row + 1) * border
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 15, y + 15), (x + size_block - 15, y + size_block - 15), 15)
                    pygame.draw.line(screen, white, (x + size_block - 15, y + 15), (x + 15, y + size_block - 15), 15)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 7.5, 15)

    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font1 = pygame.font.SysFont('tlwgtypo', 80)
        font2 = pygame.font.SysFont('tlwgtypo', 20)
        text1 = font1.render(game_over, True, white)
        text2 = font2.render('To play again press SPACE', True, white)
        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()
        text1_x = screen.get_width() / 2 - text1_rect.width / 2
        text1_y = screen.get_height() / 2 - text1_rect.height / 2 - 20
        text2_x = screen.get_width() / 2 - text2_rect.width / 2
        text2_y = screen.get_height() / 2 - text2_rect.height / 2 + 30
        screen.blit(text1, [text1_x, text1_y])
        screen.blit(text2, [text2_x, text2_y])

    pygame.display.update()
