# the example from the PyGame Documentation
import pygame
import os
import random

# TRY TO SEE IF YOU CAN GET JUST THE FACES WORKING BEFORE ADDING THE ANIMATION!!!!


pygame.init()

WIDTH = 400
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('DiceRoller')

clock = pygame.time.Clock()

#BACKGROUND_PATH = os.path.join('Dice','Background.jpg')

DICE_FACE_PATH = os.path.join('Dice','D20','Faces')

DICE_ROLLING_PATH = os.path.join('Dice','D20','RollStills')


#button setup
button_color = (196,196,196)
hover_color = (145,143,143)

button_size = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 + 125, 40,20)

dice_images = []
#for the faces
# there are 20 dice images
for i in range(1,21):
    image = pygame.image.load(os.path.join(DICE_FACE_PATH, f"{i}.png")).convert_alpha()
    resized_image = pygame.transform.scale(image, (450,450))
    dice_images.append(resized_image)


dice_rolling_images =[]
#for the animation
#there are 13 animaion frames (need to make it 22 and possible shade--
#  this is just for proof of concept)
for j in range(1,24):
    rolling_image = pygame.image.load(os.path.join(DICE_ROLLING_PATH, f"{j}.png")).convert_alpha()
    resized_rolling_image = pygame.transform.scale(rolling_image, (450,450))
    dice_rolling_images.append(resized_rolling_image)


#flags
running = True

is_rolling = False
#rolling_counter = 0

dice_num_image = dice_images[0]

while running:
    # pygame.Quit event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draws the image as the background
    #screen.blit(background, (0,0))
    #screen.blit(roll_message, (40, 200))

    #background set to white
    screen.fill((255,255,255))

    #getting keys that are pressed
    key = pygame.key.get_pressed()
    #to know if key is pressed or not. If pressed we want to roll
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_size.collidepoint(event.pos) and not is_rolling:
            is_rolling = True
            #start rolling
            rand_num = random.randint(0,19)
            rolling_counter = 0

        #seeing how many times you rolled
        #screen.blit(dice_rolling_images[rolling_counter],(-20,-80))
      
    if is_rolling:
        #showing the rolling animation 
        #seeing how many times you rolled
        #screen.blit(dice_rolling_images[rolling_counter],(200,100))
        screen.blit(dice_rolling_images[rolling_counter],(-20,-80))
        rolling_counter += 1
        #reached the end of our images
        if rolling_counter >= len(dice_rolling_images):
            is_rolling = False
            dice_num_image = dice_images[rand_num]
    else:
        #or showing the face of the die
        screen.blit(dice_num_image, (-20,-80))

    mouse_pos = pygame.mouse.get_pos()
    if button_size.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_size)
    else:
        pygame.draw.rect(screen, button_color, button_size)

    font = pygame.font.Font(None, 15)
    text = font.render("PRESS", True, "Black")
    text_rect = text.get_rect(center=button_size.center)
    screen.blit(text, text_rect)

    pygame.display.flip()
    
    #draw all our elements
    #update everything
    pygame.display.update()

    clock.tick(60) # limits fps

pygame.quit()