"""
Created on Mon Oct 24 20:24:06 2022

@author: oh-tilia
"""

import pygame
import pygame.locals
import random
from pygame import mixer
#import the Worm class, Leaf class and WormBody class from the initialization file
from worm_game_init import *


"""SET UP"""

pygame.init()
pygame.mixer.init()
pygame.font.get_init()

#colors can only be used as tuples of RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 153, 204)
GREEN = (153, 255, 51)

#window (canvas name) set up and global variables
scr_size = (750, 750)
window = pygame.display.set_mode(scr_size)                          #canvas
background = pygame.Surface(scr_size)                               #surface
pygame.display.set_caption('worm game')                             #set title of window
bg_img = pygame.image.load('media/images/game_background.jpg')      #background img source
game_icon = pygame.image.load('media/images/worm.png')                           #game icon source
pygame.display.set_icon(game_icon)                                  #set game icon on window
game_over_bg_img = pygame.image.load('media/images/game_over_background.jpg')


"""GLOBAL VARIABLES FOR GAME LOGIC"""

FPS = 60	
frames_per_sec = pygame.time.Clock()

#initialize score variable
score = 0

#initialize eaten leaves variable
leaves_eaten = 0

#initialize speed
speed = 3


"""SPRITES"""

#list that contains all the Sprites we intent to use
all_sprites_list = pygame.sprite.Group()

#worm Sprite = list of instances of the Worm class
playerWorm = [Worm(PINK,20,20)]
playerWorm[0].rect.x = 200
playerWorm[0].rect.y = 300

#adding worm Sprite to the list of Sprites
all_sprites_list.add(playerWorm)

#leaf Sprite = instance of Leaf class
leaf = Leaf(GREEN,20,20)
leaf.rect.x = random.randint(75,675)
leaf.rect.y = random.randint(75,675)

#adding leaf Sprite to the list of all Sprites
all_sprites_list.add(leaf)


"""TEXT"""

#create a font file with font name and font size
font = pygame.font.Font('media/fonts/VCR_OSD_MONO.ttf', 40)


"""SOUND DESIGN"""

#import sound effects
eaten_leaf_sound = mixer.Sound('media/sounds/boop.wav')
eaten_leaf_sound.set_volume(0.3)

#background music
pygame.mixer.music.load('media/sounds/sugar_cookie_by_starry_attic.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.1)


"""GAME LOGIC"""

def worm_movement():
    for i, part in enumerate(playerWorm[::-1]):
        if type(part) == WormBody:
            if  part.rect.x != playerWorm[::-1][i+1].rect.x :
                part.rect.x = playerWorm[::-1][i+1].rect.x 
                part.horizontal()
            elif part.rect.y != playerWorm[::-1][i+1].rect.y :
                part.rect.y = playerWorm[::-1][i+1].rect.y
                part.vertical()
            
game_running = True

#game loop
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
    
    #adding event handlers to the main program loop to respond to keystroke events
    #if allows two inputs at once so worm can move diagonally => elif
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        worm_movement()
        playerWorm[0].move_right(speed)
    elif keys[pygame.K_LEFT]:
        worm_movement()
        playerWorm[0].move_left(speed)
    elif keys[pygame.K_UP]:
        worm_movement()
        playerWorm[0].move_up(speed)
    elif keys[pygame.K_DOWN]:
        worm_movement()
        playerWorm[0].move_down(speed)
    
    #detect collision   
    collision = playerWorm[0].collide(leaf)
    if collision:
        #print("C happened.")            #log
        eaten_leaf_sound.play()
        #increment number of eaten leaves and score variables
        leaves_eaten += 1
        score += 10
        #increment speed
        if speed < 20:
            speed += 1
        #change the position of the Leaf sprite :3
        leaf.rect.x = random.randint(75,675)
        leaf.rect.y = random.randint(75,675)
        #make worm longer
        WormBody(PINK, 20, 20)
        playerWorm.append(WormBody(PINK, 20, 20))
        playerWorm[::-1][0].rect.x = playerWorm[1].rect.x - 20
        playerWorm[::-1][0].rect.y = playerWorm[1].rect.y
        all_sprites_list.add(playerWorm)
    
    #boundary
    game_over = False
    if playerWorm[0].rect.x >= 750 or playerWorm[0].rect.x <= 0:
        game_over = True
    if playerWorm[0].rect.y >= 750 or playerWorm[0].rect.y <= 0:
        game_over = True
   
    #update Sprite list
    all_sprites_list.update()

    #set background color to white
    window.fill(WHITE)

    #blit background img onto canvas            
    window.blit(bg_img, dest = (0,0))
    
    #render text that's gonna be displayed
    text_score = font.render('score:%i'%score, BLACK, True) 

    #create a rect object for the text surface
    text_score_rect = text_score.get_rect()

    #blit text onto canvas
    window.blit(text_score, dest = (740-text_score_rect.width, 20))
    
    #draw all sprites on the canvas
    all_sprites_list.draw(window)
    
    #game over screen
    if game_over == True:
        all_sprites_list.remove(playerWorm, leaf)
        window.blit(game_over_bg_img, dest = (0,0))
        text_game_over = font.render('leaves eaten:%i'%leaves_eaten, BLACK, True)
        text_game_over_rect = text_game_over.get_rect()
        window.blit(text_game_over, dest = (375- (text_game_over_rect.width/2), 600))

    #update display
    pygame.display.flip()
    
    #limit of execution of the game loop per second
    frames_per_sec.tick(FPS)
    



pygame.display.quit()
pygame.quit()