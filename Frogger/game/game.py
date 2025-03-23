import pygame , sys 
import pygame as pg 
import random as rn 
from object import *
from frog import *
from lane import * 

class Game:
    def __init__(self, screen_dimensions,screen_caption,screen_color):
        pg.init()
        pg.display.set_mode(screen_dimensions)
        pg.display.set_caption(screen_caption)

        self.screen_color = screen_color 
        self.DISPLAY = pg.display.get_surface()

        #sprite groups
        self.object_group = pg.sprite.Group()
        self.car_group = pg.sprite.Group()
        self.river_group = pg.sprite.Group()
        self.frog_group = pg.sprite.Group()

        self.all_groups = [self.object_group,self.car_group,self.river_group,self.frog_group]
        
        self.river_speeds = {}
        self.assetSetup()

    def assetSetup(self):
        Object((0,0) , (672,768), "assets/background.png",self.object_group)

        #grass
        for x in range(14):
             Object((x * 48, 384), (48,48) , "assets/redgrass.png", self.object_group)
             Object((x * 48, 672), (48,48) , "assets/redgrass.png", self.object_group)
        for x in range(28):
            Object((x * 24, 72),(24,72), "assets/grass.png",self.object_group)
        
        #lanes
        speeds = [-1.25,-1,-0.75,-0.5,-0.25,0.25,0.5,0.75,1,1.25]
        rn.shuffle(speeds)

        #river lanes 
        for y in range(5):
            y_pos = (y*48 + 144)
            new_lane = Lane((0,y_pos), self.river_group, speeds.pop(), "river")
            #self.river_group[y_pos//48] = new_lane.speed

        for y in range(5):
            y_pos = (y*48 + 432)
            Lane((0,y_pos), self.car_group,speeds.pop(), "street")
           



        self.frog = Frog((336, 672), (48,48),"assets/frog.png", self.frog_group, [self.car_group,self.river_group],self.river_speeds)
        

    
    def run(self):
        while True:
            #self.DISPLAY.fill(self.screen_color)

            self.frog.keyups = []
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYUP:
                    self.frog.keyups.append(event.key)
            
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()

                group.draw(self.DISPLAY)
            
            pg.display.update()

game = Game((672,768) , "froggertypeshift", (0,0,0))
game.run()






