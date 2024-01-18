# -*- coding: utf-8 -*-

import pygame as pg
import random


WIDTH = 400
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pg.init()
surface = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

run = True

w = 60
h = 80

trash_can = pg.image.load("trash_can.jpg")
skalert = pg.transform.scale(trash_can, (w, h))

background = pg.image.load("bakgrunn.jpg")
skalert_bg = pg.transform.scale(background, (WIDTH, HEIGHT))


x = (WIDTH-w)/2
y = HEIGHT-h

r = 20

vx = 5

font = pg.font.SysFont('Arial', 26)

def display_points(p):
    text_img = font.render(f"Antall poeng: {p}", True, BLACK)
    surface.blit(text_img,(10,10))

def display_liv(l):
    text_img = font.render(f"Antall liv: {l}", True, BLACK)
    surface.blit(text_img,(250,10))


class Ball:
    def __init__(self):
        self.r = 10
        self.x = random.randint(0+self.r, WIDTH-self.r)
        self.y = -self.r
        self.vx = 4
        self.ax = 1.001
    
    def update(self):
        self.vx *= self.ax
        self.y += self.vx
        if self.vx > 8:
            self.vx = 8
    
    def draw(self):
        pg.draw.circle(surface, BLUE, (self.x, self.y), self.r)
    
    def reset(self):
        self.y = -self.r
        self.x = random.randint(0+self.r, WIDTH-self.r)
    
ball = Ball()

p=0
liv = 3

while run:
    clock.tick(FPS)
    
    surface.blit(skalert_bg, (0,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
        x -= vx
    if keys[pg.K_RIGHT]:
        x += vx
    
    if x <= 0:
        x = 0
    elif x >= WIDTH-w:
        x = WIDTH-w
    
    
    ball.update()
    ball.draw()
    
    #pg.draw.rect(surface, RED, [x, y, w, h])
    
    surface.blit(skalert, (x,y))
    
    if y < ball.y-ball.r < HEIGHT:
        if x-ball.r < ball.x < x+w+ball.r:
            p += 1
            ball.reset()
    elif ball.y+ball.r > HEIGHT:
        liv -= 1
        ball.vx = 4
        ball.reset()
        if liv == 0:
            run = False
    
    
    
    display_liv(liv)
    display_points(p)
    
    
    pg.display.flip()





pg.quit()
print(f"Du fikk {p} poeng.")
