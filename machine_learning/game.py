import pygame
import neat
import time
import os
import random

WIN_WIDTH = 550
WIN_HEIGHT = 800

BASE_IMG = pygame.transform.scale2x(pygame.image.load('game_images/base.png'))
BACKGROUND_IMD = pygame.transform.scale2x(pygame.image.load('game_images/bg.png'))


class Bird():
    BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load("game_images/bird1.png")), pygame.transform.scale2x(
        pygame.image.load("game_images/bird2.png")), pygame.transform.scale2x(pygame.image.load("game_images/bird3.png"))]
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5  # how fast is going topm be in the air

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # for rotate the images
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.BIRD_IMAGES[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # seconds up and down for fallinfg
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if (d > 16):
            d = 16
        if d < 0:
            d -= 2
        self.y += d
        if (d < 0 or self.y < self.height + 50):
            if (self.tilt < self.MAX_ROTATION):
                self.tilt = self.MAX_ROTATION
        else:
            if (self.tilt > -90):
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1
        if (self.img_count < self.ANIMATION_TIME):
            self.img = self.BIRD_IMAGES[0]
        elif (self.img_count < self.ANIMATION_TIME*2):
            self.img = self.BIRD_IMAGES[1]
        elif (self.img_count < self.ANIMATION_TIME*3):
            self.img = self.BIRD_IMAGES[2]
        elif (self.img_count < self.ANIMATION_TIME*4):
            self.img = self.BIRD_IMAGES[1]
        elif (self.img_count < self.ANIMATION_TIME*4 + 1):
            self.img = self.BIRD_IMAGES[0]
            self.img_count = 0
        if (self.tilt <= -80):
            self.img = self.BIRD_IMAGES[1]
            self.img_count = self.ANIMATION_TIME*2
        #I just rotate the image related with the center of the screen and not from the corner
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image,new_rect.topleft)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
class Pipe():
    PIPE_IMG = pygame.transform.scale2x(pygame.image.load('game_images/pipe.png'))
    GAP = 200
    VEL = 5
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True) #I flip one image
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed  = False #For knowing if there is a colision with the bird
        self.set_height()

def draw_window(win, bird):
    win.blit(BACKGROUND_IMD,(0,0)) #The corner of the image
    bird.draw(win)
    pygame.display.update()

def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird(200,200)
    run = True
    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        bird.move()
        draw_window(win, bird)

main()