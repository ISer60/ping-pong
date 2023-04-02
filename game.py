from pygame import *

class GameSprite(sprite.Spite):
    def _init_(self,spite_image,x=0,y=0,wight=50,height=50):
        super()._init_()
    self.image=transform.scale(image.load(sprite_image),(wight,height))
    selfreact
BG_COLOR = (220,100,220)
WIDTH, HEIGHT = 600,480