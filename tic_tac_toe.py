import pygame
import sys

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
width = height = 40
mas = [['0'] * 3 for i in range(3)]

while True:
    for event in pygame.event.get():
        for row in range(3):
            for col in range(3):
                x = col * size_block + (col + 1) * border
                y = row * size_block + (row + 1) * border
                pygame.draw.rect(screen, red, (x, y, size_block, size_block))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()