import pygame
from pygame.locals import *
import random
import math
pygame.init()
pygame.font.init()
counter=random.randint(1,4)
# check whether font is initialized
# or not
score=0
pygame.font.get_init()
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Game")
amplitude = 10  # Adjust this value to control the amplitude of the oscillation
speed = 0.1  # Adjust this value to control the speed of the oscillation
clock = pygame.time.Clock()


x = 50
y = 50
random.seed(150)
x1 = random.randint(100,400)
y1 = random.randint(100,400)
width = 50
height = 50
vel = 5



# setting center for the first text

rect2= pygame.draw.rect(win, (0,255,0), (x1, y1, width, height)) 

run = True

while run:
    
    counter=random.randint(1,4)
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)
    score1="Score "+str(score)
    text1 = font1.render(score1, True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (60, 60)
    win.blit(text1, textRect1)
    pygame.display.update()
    background_colour = (255,255,255)
    pygame.time.delay(10)
    rect1 = pygame.Rect(100, 100, 50, 50)
    rect2 = pygame.Rect(100, 100, 50, 50)   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update the target position
    pygame.display.update()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill(background_colour)  # Fills the screen with black
    rect1= pygame.draw.rect(win, (255,0,0), (x, y, width, height))    
    rect2= pygame.draw.rect(win, (color1,color2,color3), (x1, y1, width, height))
    if counter==1:
        rect2= pygame.draw.rect(win, (color1,color2,color3), (x1+2, y1+2, width, height))
    elif counter==2:
        rect2= pygame.draw.rect(win, (color1,color2,color3), (x1-2, y1-2, width, height))
    elif counter==3:
         rect2= pygame.draw.rect(win, (color1,color2,color3), (x1-2, y1+2, width, height))
    elif counter==4:
         rect2= pygame.draw.rect(win, (color1,color2,color3), (x1+2, y1-2, width, height))
    collide=pygame.Rect.colliderect(rect1, rect2)
    if collide:
        x1=random.randint(150,500)
        y1=random.randint(150,500)
        rect2= pygame.draw.rect(win, (color1,color2,color3), (x1, y1, width, height)) 
           
        score+=1
    pygame.display.update() 
    
    
pygame.quit()