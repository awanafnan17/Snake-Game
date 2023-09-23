import pygame
import random
import os


pygame.mixer.init()
pygame.mixer.music.load('32.mp3')
pygame.mixer.music.play()

pygame.init()

# Specifying Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (200, 203, 255)
black = (0, 0, 0)
unknown = (154,207,229)

# Setting Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

## Background Image
# bg = pygame.image.load('bg.jpg')
# bg = pygame.transform.scale(bg, (screen_width, screen_height)).convert_alpha()
# bg2 = pygame.image.load('bg2.jpg')
# bg2 = pygame.transform.scale(bg2, (screen_width, screen_height)).convert_alpha()





exit_Game = False
game_Over = False
clock = pygame.time.Clock()


# Game Title
pygame.display.set_caption("SnakesWithAwan")
pygame.display.update()
font = pygame.font.SysFont(None, 55)


def score_screen(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):   
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_Game = False
    while not exit_Game:
        gameWindow.fill(blue)
        score_screen("Welcome to the Snake Game!", white, 180, 250)
        score_screen("Press Space Bar to Play", white, 230, 290)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_Game = True
                # exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gmeloop()
        # gameWindow.blit(bg, (0, 0))
  

        pygame.display.update()
        clock.tick(60)
        




# Game Loop
def gmeloop():

    # Game Variables
    snake_x = 45
    snake_y = 55
    snake_size = 15
    food_size = 11
    exit_Game = False
    game_Over = False
    clock = pygame.time.Clock()
    fps = 60
    velocity_x = 0
    velocity_y = 0
    vel = 4
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    snk_list = []
    snk_len = 1
    if(not os.path.exists("highscore.txt")):
        with open('highscore.txt', 'w') as f:
            f.write("0")
    with open('highscore.txt', 'r') as f:
        hscore = f.read()

    while not exit_Game:
        if game_Over:
            score_screen("Game Over, Enter to start over!", red, 200, 250)
            with open('highscore.txt', 'w') as f:
                f.write(str(hscore))
            for event in pygame.event.get():
                    exit_Game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_Game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -vel
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = vel
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -vel
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x 
            snake_y += velocity_y 

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                vel += 0.05
                snk_len += 3
                if score > int(hscore):
                    hscore = score



            gameWindow.fill(unknown)
            # gameWindow.blit(bg2, (0, 0))
            score_screen("Score: " + str(score) + "  Highscore: " + str(hscore), red, 5, 5)


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

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_Over = True
                
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()