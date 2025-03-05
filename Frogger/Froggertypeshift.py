import pygame
from pygame import *
pygame.init()


width = 1300
height = 800
screen = display.set_mode((width,height))

display.set_caption('Frogger')


froggypic = image.load("frog.png")
froggypic = transform.scale(froggypic,(50,50))
frogRect = Rect(650,750,50,50)


#cars = []
#cars.append(Rect(200,200,40,40))

mixer_music.load("backgroundmusic.mp3")
mixer_music.play(-1)
jump = mixer.Sound("jumpnoise.mp3")

startGame = True
while startGame:

    for event in pygame.event.get():
        if event.type == QUIT:
            startGame = False
        
        if event.type == KEYDOWN:
            
            if event.key == K_DOWN:
                jump.play()
                frogRect.move_ip(0,50)
            
            if event.key == K_UP:
                jump.play()
                frogRect.move_ip(0,-50)
            
            if event.key == K_RIGHT:
                jump.play()
                frogRect.move_ip(50,0)
            
            if event.key == K_LEFT:
                jump.play()
                frogRect.move_ip(-50,0)

    screen.fill("black")
    screen.blit(froggypic,frogRect)
    
    pos = 0
    y = 50
    while pos < 4:
        kerb = draw.rect(surface=screen,color=(128,128,128),rect=(0,600,1300,50))
        pos = pos + 1 
    display.flip()
pygame.quit()








