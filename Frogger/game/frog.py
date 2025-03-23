import pygame as pg 
from object import * 

class Frog(Object):
    def __init__(self,pos,size,image,group,collision_groups,river_speeds):
        super().__init__(pos,size,image,group)

        self.keyups = []

        self.collision_groups = collision_groups

        self.river_speeds = river_speeds
        self.x_speed = 0

    def moveFrog(self):
        x = self.pos[0]
        y = self.pos[1]
        jump_sfx = pg.mixer.Sound("assets/jumpnoise.mp3")

        if pg.K_UP in self.keyups:
            y -= 48
            jump_sfx.play()
        
        if pg.K_DOWN in self.keyups:
            y += 48
            jump_sfx.play()
        if pg.K_LEFT in self.keyups:
            x -= 48
            jump_sfx.play()
        if pg.K_RIGHT in self.keyups:
            x += 48 
            jump_sfx.play()
        if x <= -48 or x >= 48*14 or y >48*16:
            self.killFrog()
            return 

        self.pos = (x,y)

    def checkCollisions(self):
        self.setImage()

        collided = False
        for sprite_group in self.collision_groups:
            if pg.sprite.spritecollideany(self,sprite_group):
                collided = True
        
        lane = self.pos[1]//48
        if collided:
            if lane < 8:
                self.x_speed = self.river_speeds[lane]
            else:
                self.killFrog()
        else:
            self.x_speed = 0 
            if lane < 8:
                self.killFrog()

    def killFrog(self):
        self.x_speed = 0
        self.pos = (336,672)
        self.image_directory = "assets/frog.png"
        self.setImage()

    def update(self):
        self.setImage()
        self.moveFrog()
        self.checkCollisions()