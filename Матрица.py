import os
import pygame as pg
from random import choice, randrange


class Symbol:
    def init(self, x, y):
        self.x, self.y, = x,y
        self.value = choice(green-katakana)

    def draw(self):
        surface.blit(sekf.value, (self.x, self.y))


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 140

pg.init()
surface = pg.displey.ser_mode(RES)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Sysfont('ms mincho', FONT_SIZE, bold=True)
green_katakana = [font.render(char, True, pg.Color('green')) for char in katakana]

symbol = Symbol(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)
while True:
    surface.fill(pg.Color('black'))

    symbol.draw()

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.displey.flip()
    clock.tick(60)













