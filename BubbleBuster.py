import pygame #Library for making game creation easier
import sys #Library to help close a program
from pygame.locals import * #Gets local files as resources

pygame.init() #Initialize

screen = pygame.display.set_mode((640, 460)) #Screen dimensions, set_mode immediately turns on the screen of specified width and height dimensions
pygame.display.set_caption("Bubble Buster") #Sets name of specified window
screen.fill((255, 255, 255)) #Fills the screen with a color based on RGB syntax
font = pygame.font.SysFont(None, 36) #Chooses a font style for text-based functions

main_clock = pygame.time.Clock()
score = 0

lives = 3
alive = True

player = pygame.Rect(290, 400, 60, 10) #Gives variable player the dimensions of a rectangle with arguments (initial x, initial y, length, width). Note initial y is from the top
player_speed = 4

move_left = False
move_right = False

def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), player) #Draws a rectangle with arguments of (screen choice, (R, G, B), (dimensions))

def draw_screen():
    screen.fill((255, 255, 255))

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)


x_position = 380
y_position = 320
last_x = x_position
last_y = y_position
ball_can_move = False

speed = [3, -3]

all_bubbles = []
bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position

    for rows in range(0, 3):
        for columns in range (0, 10):
            bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble_x, bubble_y), bubble_radius, bubble_edge) #Draws a circle with arguments of (screen choice, (R, G, B), (center x-axis, center y-axis), circle radius, circle edge)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position

create_bubbles()

def draw_bubbles():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.x, bubble.y), bubble_radius, bubble_edge)

while True:
    for event in pygame.event.get(): #event.get checks for if an event was received (Only hardware?)
        if event.type == QUIT: #Press the X button (Close window)
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:#Press a keyboard key
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_right = True
                move_left = False
        if event.type == KEYUP: #Release a keyboard key
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if not alive:
                if event.key == K_RETURN:
                    lives = 3
                    alive = True
                    score = 0
                    ball_can_move = False
                    for x in range(0, len(all_bubbles)):
                        all_bubbles.pop()
                    create_bubbles()

    main_clock.tick(90) #Maximum amount of frames witin program

    if move_left and player.left > 0: #Functions left and right are reference points for the edges of the rectangle
        player.x -= player_speed #Function x affects the object's x position
    if move_right and player.right < 640:
        player.x += player_speed

    if ball_can_move:
        last_x = x_position #Records last positions of ball
        last_y = y_position

        x_position += speed[0] #Changes position of ball based on speed values
        y_position += speed[1]
        if ball.x <= 0: #Checks for wall collisions
            x_position = 6
            speed[0] = -speed[0]
        elif ball.x >= 640:
            x_position = 634
            speed[0] = -speed[0]
        if ball.y <= 0:
            y_position = 6
            speed[1] = -speed[1]
        elif ball.y >= 460:
            lives -= 1
            ball_can_move = False

        if ball.colliderect(player): #Checks for player collisions
            y_position -= 6
            speed[1] = -speed[1]

        move_direction = ((x_position - last_x), (y_position - last_y)) #Tracks ball direction by vector
        print(move_direction)

        for bubble in all_bubbles: #Test collisions with bubbles
            if ball.colliderect(bubble):
                if move_direction[1] > 0:
                    speed[1] = -speed[1]
                    y_position -= 10
                elif move_direction[1] < 0:
                    speed[1] = -speed[1]
                    y_position += 10
                all_bubbles.remove(bubble)
                score += 100
                break
    else:
        x_position = player.x + 30
        y_position = 380

    if lives <= 0:
        alive = False

    draw_screen()
    draw_player()
    draw_bubbles()
    ball = pygame.draw.circle(screen, (0, 0, 0), (x_position, y_position), 5, 0)

    if alive:
        draw_text('Score: %s' % (score), font, screen, 5, 5) #Text with arguments ("Text", font, screen, initial x-axis, initial y-axis)
        draw_text('Lives: %s' % (lives), font, screen, 540, 5)
    else:
        draw_text('Game Over', font, screen, 255, 5)
        draw_text('Press Enter to Play Again', font, screen, 180, 50)

    pygame.display.update()# Updates the display/window