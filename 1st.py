import random
import pygame


# Initializing
pygame.init()





white = (255, 255, 255)
red = (255, 0, 0)
blue = (200, 203, 255)
black = (0, 0, 0)
unknown = (154,207,229)


# Creating Window
width = 900
height = 600
gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")
pygame.display.update()



def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])



def gameLoop():
    # Setting different variables
    exit_Game = False
    game_Over = False
    clock = pygame.time.Clock()
    fps = 60
    snake_x = 45
    snake_y = 55
    snake_size = 15
    food_size = 11
    velocity_x = 0
    velocity_y = 0
    vel = 4
    food_x = random.randint(20, width/2)
    food_y = random.randint(20, height/2)
    snk_list = []
    snk_len = 1





    # Creating Game Loop
    while not exit_Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_Game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    velocity_y = vel
                    velocity_x = 0

                if event.key == pygame.K_UP:
                    velocity_y = -vel
                    velocity_x = 0

                if event.key == pygame.K_LEFT:
                    velocity_x = -vel
                    velocity_y = 0

                if event.key == pygame.K_RIGHT:
                    velocity_x = vel
                    velocity_y = 0

        snake_x += velocity_x
        snake_y += velocity_y


        if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
            snk_len += 10
            food_x = random.randint(20, width/2)
            food_y = random.randint(20, height/2)




        
        gameWindow.fill(unknown)
        plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])


        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_len:
            del snk_list[0]

        if head in snk_list[:-1]:
            game_Over = True

        if snake_x<0 or snake_x<width or snake_y<0 or snake_y<height:
            game_Over = True




        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()



gameLoop()