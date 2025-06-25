import pygame

from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 900
ground_scroll = 0
scroll_speed = 2
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pony Escape")
background_image=pygame.image.load("orangesky.jpg")
ground_image=pygame.image.load("ground.png")
flying=False
gameover=False

class Pony(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(3):
            img=pygame.image.load(f"pony{i+1}.png") # loads images in order with numbering
            self.images.append(img) # puts each image to the list
        self.image=self.images[self.index] # record of current image
        self.rect=self.image.get_rect()
        self.velocity=0
    def update(self):
        if flying:
            self.velocity += 0.5 # make the pony gradually fall down
            if self.velocity > 8:
                self.velocity=8
            if self.rect.bottom<700:
                self.rect.y+=self.velocity
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==True:
                self.velocity=-10 # if mouse is pressed, pony goes up
            self.counter+=1
            flapdown=5
            if self.counter>flapdown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

Ponygroup=pygame.sprite.Group()
