import pygame
import random
import math
import sys
from pygame.locals import *

pygame.init()

file_variable = open("Map.txt", "w")
string = """001011000
111111100001
010101
111010001
"""
file_variable.write(string)
file_variable.close()

screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))

main_clock = pygame.time.Clock()

x_pos = 10
y_pos = 10
rectangles = []

file_variable = open("Map.txt", "r")

for line in file_variable:
    line = line.rstrip()
    for x in range(0, len(line)):
        if(int(line[x]) == 0):
            x_pos += 40
        elif(int(line[x]) == 1):
            x_pos += 40
            rectangle = pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, 30, 10))
            rectangles.append(rectangle)
        else:
            pass
    x_pos = 10
    y_pos += 20

file_variable.close()

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    main_clock.tick(50)
    screen.fill((255, 255, 255))
    for rectangle in rectangles:
        pygame.draw.rect(screen, (0, 0, 0), rectangle)
    pygame.display.update()