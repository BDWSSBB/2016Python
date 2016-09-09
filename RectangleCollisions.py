import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()

player = pygame.Rect((30, 40, 50, 20))
x = 50
y = 20

list_of_rects = []
rectangle_a = pygame.Rect((60, 60, 60, 10))
rectangle_b = pygame.Rect((460, 260, 60, 30))
rectangle_c = pygame.Rect((300, 150, 20, 20))
rectangle_d = pygame.Rect((150, 200, 40, 10))
list_of_rects.append(rectangle_a)
list_of_rects.append(rectangle_b)
list_of_rects.append(rectangle_c)
list_of_rects.append(rectangle_d)

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    player = pygame.Rect(x, y, 50, 20)

    #Do the player and other rectangles collide?
    if player.collidelist(list_of_rects) >= 0:
        collision_index = player.collidelist(list_of_rects)
        print("I'm colliding with " + str(list_of_rects[collision_index]))
    else:
        print("I'm not colliding with on screen elements.")

    main_clock.tick(1200)
    pygame.draw.rect(screen, (0, 0, 0), (player), 0)
    for rectangle in list_of_rects:
        pygame.draw.rect(screen, (0, 0, 0), (rectangle.x, rectangle.y, rectangle.width, rectangle.height), 2)
    pygame.display.update()