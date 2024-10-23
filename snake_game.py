# In this game, a snake catches the maximum number of fruits without hitting the wall or itself
# AI takes care of which ways for snakes to go

"""
# #1: importing the necessary libraries
import pygame
import time
import random

# displaying Score function
def show_score(game_window, score, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # displaying text 
    game_window.blit(score_surface, score_rect)

def game_over(game_window, window_x, window_y, score, red):
    # create font object
    my_font = pygame.font.SysFont('times new roman', 50)

    # create a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is: '+str(score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip() # this is a function that updates the contents of the entire display surface (the game window) on the screen. 

    # after 2 seconds, we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()




# Main Function
def game():

    snake_speed = 15

    # window size 
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white =  pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)


    # #2: After importing libraries we need to initialize Pygame using pygame.init() method
    # initialize pygame
    pygame.init()

    # initialize game window
    pygame.display.set_caption('GeekforGeeks Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()


    # #3: initialize snake position and its size
    # define the snake default position 
    snake_position = [100, 50]

    # define first 4 blocks of snake body 
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]]

    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True
    # setting default snake direction towards right
    direction = 'RIGHT'
    change_to = direction

    # #4: a function to display the score 
    # initial score
    score = 0
    while True:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # if two keys pressed simultaneously, we don't want snake to move into two directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # move the snake 
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

        # snake body growing mechanism
        # if fruits and snakes collide then scores will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spwan = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        
        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        # game over condition
        # check if it hits the wall
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over(game_window, window_x, window_y, score, red)    
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(game_window, window_x, window_y, score,red)    

        # check if it hits itself
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, window_x, window_y, score, red)

        # displaying score continuously
        show_score(game_window, score, white, 'times new roman', 20)

        # refresh game screen
        pygame.display.update()

        # Frame PerSecond / Refresh Rate
        fps.tick(snake_speed)

game()
"""

# importing libraries
import pygame
import time
import random


def cell_score(cell, fruit_cell, window_x, window_y):
    # calculate the straight distance between a cell and the fruit
    distance = ((fruit_cell[0] - cell[0])^2 + (fruit_cell[1] - cell[1])^2)^(1/2)

    center_x = window_x / 2
    center_y = window_y / 2

    danger_wall_score = (window_x + window_y) - (abs(window_x - center_x) + abs(window_y - center_y))



# displaying Score function
def show_score(choice, color, font, size, game_window, score):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over(game_window, score, window_x, window_y, red):
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

def game():
    snake_speed = 10

    # Window size
    window_x = 700
    window_y = 500

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Welcome to the Snake Game 480')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                    random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        # If two keys pressed simultaneously
        # we don't want snake to move into two 
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position)) # snake making forward movement
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        print(snake_position[0], snake_position[1])
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over(game_window, score, window_x, window_y, red)
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over(game_window, score, window_x, window_y, red)

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, score, window_x, window_y, red)

        # displaying score continuously
        show_score(1, white, 'times new roman', 20, game_window, score)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)

game()