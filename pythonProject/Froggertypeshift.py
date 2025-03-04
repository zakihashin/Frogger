import pygame
from pygame import *
pygame.init()


width = 600
height = 400
screen = display.set_mode((width,height))

display.set_caption('Frogger')


froggypic = image.load("frog.png")
froggypic = transform.scale(screen,(100,100))
frogRect = Rect(100,0,10,10)

cars = []
cars.append(Rect(200,200,40,40))


startGame = True
while startGame:

    for event in pygame.event.get():
        if event.type == QUIT:
            startGame = False

    screen.fill("red")
    screen.blit(froggypic,frogRect)
    display.flip()
pygame.quit()








