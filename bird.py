import pygame
from pygame.locals import *
class Bird(pygame.sprite.Sprite):
    def __init__(self,x_cord,y_cord,animation_set):
        super().__init__()
        self.frames = animation_set
        self.vel = 0
        self.counter = 0
        self.index = 0

        if (len(self.frames) != 0):
         self.image = self.frames[self.index]
         self.rect = self.image.get_rect()
         self.rect.center = [x_cord, y_cord]
   
    @property
    def animate_flapping(self):
        """Cycle through our animation frames and rotates bird"""

        #Determines speed we loop through our flappybird frames
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.frames):
                self.index = 0
        self.image = self.frames[self.index]

        #Rotates our flappy bird image 
        self.image = pygame.transform.rotate(self.frames[self.index], self.vel * -4)

    def player_movement(self,g,jump=0):
        """Handles player inputs and gravity"""
        
        self.vel += g

        #A cap placed on the max velocity a player can have
        if self.vel > 10:
            self.vel = 10

        #If player hits floor, they can no longer move. 
        if self.rect.bottom < 900:
            self.rect.y += int(self.vel)

        #Gravity pulls down on the bird
        if jump != 0:
         self.vel = 0
         self.vel += jump

        #Player jumped
        else:
            self.vel += jump

        self.animate_flapping
        
        

    










