"""
Created on Tue Oct 25 14:30:41 2022

@author: oh-tilia
"""

import pygame


#colors can only be used as tuples of RGB values
WHITE = (255, 255, 255)
GREEN = (153, 255, 51)


#creating class that represents our worm derived from a Sprite
class Worm(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #call the parent class (Sprite) constructor
        super().__init__()
        
        #self refers to the current object
        self.image = pygame.Surface([width, height])
        self.rect = self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
        #draw the worm Sprite (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #blit img unto Worm
        self.image = pygame.image.load('media/images/worm.png').convert_alpha()
        
        #fetch the rectangle object
        self.rect = self.image.get_rect()
        
        
    #adding methods to the class in order to move the Worm Sprite
    def move_right(self, pixels):
        self.image = pygame.image.load('media/images/worm.png').convert_alpha()
        self.rect.x += pixels
    
    def move_left(self, pixels):
        self.image = pygame.image.load('media/images/worm_heading_left.png').convert_alpha()
        self.rect.x -= pixels
    
    def move_up(self, pixels):
        self.image = pygame.image.load('media/images/worm_heading_up.png').convert_alpha()
        self.rect.y -= pixels
    
    def move_down(self, pixels):
        self.image = pygame.image.load('media/images/worm_heading_down.png').convert_alpha()
        self.rect.y += pixels


    #adding collision method to detect when Worm collides with Leaf
    def collide(self, leaf):
        if (self.rect.x >= leaf.rect.x -20 and self.rect.x <= leaf.rect.x +20) and (self.rect.y >= leaf.rect.y -20 and self.rect.y <= leaf.rect.y + 20):
            return True

#    def colliderect(self, leaf):
#        pass


class WormBody(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
        #draw the WormBody (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #blit img unto WormBody
        self.image = pygame.image.load('media/images/worm_body_sideways.png').convert_alpha()
        
        #fetch the rectangle object
        self.rect = self.image.get_rect()
        
        
    #adding methods to the class in order to move the Sprite
    def horizontal(self):
        self.image = pygame.image.load('media/images/worm_body_sideways.png').convert_alpha()

    def vertical(self):
        self.image = pygame.image.load('media/images/worm_body_updown.png').convert_alpha()


#creating class that represents our leaf derived from a Sprite
class Leaf(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.rect = self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
        #draw the Leaf (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #blit img unto Leaf
        self.image = pygame.image.load('media/images/leaf.png').convert_alpha()
        
        #fetch the rectangle object
        self.rect=self.image.get_rect()
