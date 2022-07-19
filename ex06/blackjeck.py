from xml.sax import default_parser_list
import pygame as pg
import sys
from random import randint


def Hand():
    count = 0
    hand = [[False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False]]
    while count < 2:
        soot = randint(0, 3)
        number = randint(0, 12)
        if hand[soot][number] != True:
            hand[soot][number] = True
            count += 1

    return hand


def Return_sum(list):

    sum = 0

    for i in range(4):
        for j in range(13):
            if list[i][j] == True:
                if j == 0:
                    if (sum + 11) > 21:
                        sum += 1
                    else :
                        sum += 11 

                if j > 9:
                    sum += 10
                    continue
                sum += j + 1

    return sum


def Hit(hand):
    count = 0
    while count < 2:
        soot = randint(0, 3)
        number = randint(0, 12)
        if hand[soot][number] != True:
            hand[soot][number] = True
            count += 1

    return hand


def Judge(m, d, mw, dw, d_hand):
    if d < 17:
        d_hand = Hit(d_hand)
        d = Return_sum(d_hand)

    if (m < 22) and (m > d):
        mw += 1
    elif (d < 22) and (m < d):
        dw += 1


def main():
    mwin = 0
    dwin = 0

    pg.display.set_caption("ブラックジャック")
    screen_sfc=pg.display.set_mode((1600,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("fig/bg.jpg")
    bgimg_rct=bgimg_sfc.get_rect()

    hitimg_sfc=pg.image.load("fig/hit.png")
    hitimg_sfc=pg.transform.rotozoom(hitimg_sfc, 0, 0.3)
    hitimg_rct=hitimg_sfc.get_rect()
    hitimg_rct.center=1200,600

    stdimg_sfc=pg.image.load("fig/stand.png")
    stdimg_sfc=pg.transform.rotozoom(stdimg_sfc, 0, 0.3)
    stdimg_rct=stdimg_sfc.get_rect()
    stdimg_rct.center=1400,600

    
    while True:
        m_hand = Hand()
        d_hand = Hand()
        m_num = Return_sum(m_hand)
        d_num = Return_sum(d_hand)
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(hitimg_sfc,hitimg_rct)
        screen_sfc.blit(stdimg_sfc,stdimg_rct)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if hitimg_rct.collidepoint(event.pos):
                    m_hand = Hit(m_hand)
                    m_num = Return_sum(m_hand)
                elif stdimg_rct.collidepoint(event.pos):
                    Judge(m_num, d_num, mwin, dwin, d_hand)

        if (mwin == 5) or (dwin == 5):
            return

        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()