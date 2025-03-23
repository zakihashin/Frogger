import pygame as pg 

class Object(pg.sprite.Sprite):
    def __init__(self,pos,size,image_directory,group):
        super().__init__(group)

        self.pos = pos 
        self.size = size

        self.image_directory = image_directory

    def setImage(self):
        self.image = pg.image.load(self.image_directory)
        self.image = pg.transform.scale(self.image,self.size)
        self.surf = pg.Surface(self.size).convert_alpha()
        self.surf.fill((0,0,0,0))
        self.rect = self.surf.get_rect(topleft = self.pos)
        self.surf.blit(self.image, (0,0) )

    def update(self):
        self.setImage()