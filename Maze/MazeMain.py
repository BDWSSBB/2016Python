from MazeList import MazeList
from MazeWalls import WallKeycode

import pygame
import random
import math
import sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Infinite Mazes")
screen = pygame.display.set_mode((240, 240))
font = pygame.font.SysFont(None, 12)

def draw_text(display_string, font, screen, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    screen.blit(text_display, (x_pos, y_pos))

main_clock = pygame.time.Clock()

current_maze_template = ["", "", "", "", "", ""] #Template of a naked maze
current_maze_indicators = [[0, 0], [0, 0]]
player_position = [0, 0]
player_position_letter = "a"
player_position_number = "0"
goal_position = [0, 0]

w_key_pressed = False
a_key_pressed = False
s_key_pressed = False
d_key_pressed = False

def make_new_maze():
    global current_maze_template
    global current_maze_indicators
    global player_position
    global goal_position

    new_maze_ID = random.randrange(0, 9)
    for maze_paste_step in range(0, 6):
        current_maze_template[maze_paste_step] = MazeList.maze_layouts[new_maze_ID][maze_paste_step]
        #print(current_maze_template[maze_paste_step]) #Debug
    for maze_paste_step in range (0, 2):
        current_maze_indicators[0][maze_paste_step] = MazeList.maze_indicators[0][new_maze_ID][maze_paste_step]
        current_maze_indicators[1][maze_paste_step] = MazeList.maze_indicators[1][new_maze_ID][maze_paste_step]
    #print(current_maze_indicators[0]) #Debug
    #print(current_maze_indicators[1]) #Debug
    player_position = [random.randrange(0, 6), random.randrange(0, 6)]
    goal_position = [random.randrange(0, 6), random.randrange(0, 6)]
    while player_position == goal_position:
        goal_position = [random.randrange(0, 6), random.randrange(0, 6)]

def draw_player():
    pygame.draw.rect(screen, (255, 255, 255), (player_position[0] * 40 + 11, player_position[1] * 40 + 11, 18, 18))

def draw_tiles():
    for tiles_creation_y in range (0, 6):
        for tiles_creation_x in range (0,6):
            pygame.draw.rect(screen, (35, 76, 93), (tiles_creation_x * 40 + 11, tiles_creation_y * 40 + 11, 18, 18))

def draw_goal():
    pygame.draw.rect(screen, (160, 19, 39), (goal_position[0] * 40 + 11, goal_position[1] * 40 + 11, 18, 18))

def draw_indicators():
    pygame.draw.circle(screen, (146, 192, 127), (current_maze_indicators[0][0] * 40 + 20, current_maze_indicators[0][1] * 40 + 20), 18, 4)
    pygame.draw.circle(screen, (146, 192, 127), (current_maze_indicators[1][0] * 40 + 20, current_maze_indicators[1][1] * 40 + 20), 18, 4)

make_new_maze()

while True:
    if player_position == goal_position:
        make_new_maze()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_w and w_key_pressed == False:
                if WallKeycode.tile_walls[player_position_number][0] == True:
                    w_key_pressed = True
                else:
                    player_position[1] -= 1
                    w_key_pressed = True

            if event.key == K_a and a_key_pressed == False:
                if WallKeycode.tile_walls[player_position_number][3] == True:
                    a_key_pressed = True
                else:
                    player_position[0] -= 1
                    a_key_pressed = True

            if event.key == K_s and s_key_pressed == False:
                if WallKeycode.tile_walls[player_position_number][2] == True:
                    s_key_pressed = True
                else:
                    player_position[1] += 1
                    s_key_pressed = True

            if event.key == K_d and d_key_pressed == False:
                if WallKeycode.tile_walls[player_position_number][1] == True:
                    d_key_pressed = True
                else:
                    player_position[0] += 1
                    d_key_pressed = True

        if event.type == KEYUP:
            if event.key == K_w:
                w_key_pressed = False

            if event.key == K_a:
                a_key_pressed = False

            if event.key == K_s:
                s_key_pressed = False

            if event.key == K_d:
                d_key_pressed = False

    main_clock.tick(600)

    player_position_letter = current_maze_template[player_position[1]][player_position[0]]
    for number_letter_comparison in range (0, 16):
        if player_position_letter == WallKeycode.tile_characters[number_letter_comparison]:
            player_position_number = number_letter_comparison

    screen.fill((9, 14, 34))
    draw_tiles()
    draw_player()
    draw_goal()
    draw_indicators()

    pygame.display.update()