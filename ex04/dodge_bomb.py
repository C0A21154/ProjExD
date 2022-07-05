import random
from turtle import right
import pygame as pg
import sys

def main():
    vx, vy = 1, 1
    
    pg.display.set_caption("逃げろ！！こうかとん")
    
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    clock = pg.time.Clock()
    bgimg_sfc = pg.image.load("fig/bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    bdimg_sfc = pg.image.load("fig/6.png")
    bdimg_sfc = pg.transform.rotozoom(bdimg_sfc, 0, 2.0)
    bdimg_rct = bdimg_sfc.get_rect()
    bdimg_rct.center = 900,400

    bmimg_sfc = pg.Surface((20, 20))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_sfc.set_colorkey(0)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_type = pg.key.get_pressed()
        if key_type[pg.K_UP] == True:
            bdimg_rct.centery -=1
        elif key_type[pg.K_DOWN] == True:
            bdimg_rct.centery +=1
        elif key_type[pg.K_LEFT] == True:
            bdimg_rct.centerx -=1
        elif key_type[pg.K_RIGHT] == True:
            bdimg_rct.centerx +=1

        if bound(bdimg_rct, screen_rct) != (1, 1):
            if key_type[pg.K_UP] == True:
                bdimg_rct.centery +=1
            elif key_type[pg.K_DOWN] == True:
                bdimg_rct.centery -=1
            elif key_type[pg.K_LEFT] == True:
                bdimg_rct.centerx +=1
            elif key_type[pg.K_RIGHT] == True:
                bdimg_rct.centerx -=1

        screen_sfc.blit(bdimg_sfc, bdimg_rct)

        bmimg_rct.move_ip(vx, vy)
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        yoko, tate = bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate 

        if bdimg_rct.colliderect(bmimg_rct) : return
        
        pg.display.update()
        clock.tick(1000)

def bound(rct, scr_rct):

    yoko, tate = +1, +1

    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
