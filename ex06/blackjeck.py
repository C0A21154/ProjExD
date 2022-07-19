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


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) 
        self.rct = self.sfc.get_rect()  
        self.bgi_sfc = pg.image.load(image)   
        self.bgi_rct = self.bgi_sfc.get_rect()
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Card:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Hit_s:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Stand_s:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Back:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

def main():
    mwin = 0
    dwin = 0

    scr = Screen("ブラックジャック", (1600, 900), "fig/bg.jpg")
    hit_s = Hit_s("fig/hit.png", 0.3, (1200,600))
    std = Stand_s("fig/stand.png", 0.3, (1400,600))
    bak = Back("fig/back.png", 0.8, (900,200))
    
    m_hand = Hand()
    d_hand = Hand()
    m_num = Return_sum(m_hand)
    d_num = Return_sum(d_hand)
    ct = 1
    m_card = []
    d_card = []

    for i in range(4):
        for j in range(13):
            if (m_hand[i][j] == True) and ct == 1:
                a = i
                if i == 1:
                    a = 13
                elif i == 2:
                    a = 26
                elif i == 3:
                    a = 39
                n = a + j
                m_card.append(n)
                ct += 1
            if (m_hand[i][j] == True) and ct == 2:
                a = i
                if i == 1:
                    a = 13
                elif i == 2:
                    a = 26
                elif i == 3:
                    a = 39
                n = a + j
                m_card.append(n)
                break
    mc1 = Card(f"fig/{m_card[0]}.png", 0.3, (600, 500))
    mc2 = Card(f"fig/{m_card[1]}.png", 0.3, (900, 500))

    for i in range(4):
        for j in range(13):
            if (d_hand[i][j] == True) and ct == 1:
                a = i
                if i == 1:
                    a = 13
                elif i == 2:
                    a = 26
                elif i == 3:
                    a = 39
                n = a + j
                d_card.append(n)
                ct += 1
            if (m_hand[i][j] == True) and ct == 2:
                a = i
                if i == 1:
                    a = 13
                elif i == 2:
                    a = 26
                elif i == 3:
                    a = 39
                n = a + j
                d_card.append(n)
                break
        
    dc1 = Card(f"fig/{d_card[0]}.png", 0.3, (600, 200))
    dc2 = Card(f"fig/{d_card[1]}.png", 0.3, (900, 200))

    while True:
        scr.blit()
        hit_s.blit(scr)
        std.blit(scr)
        dc1.blit(scr)
        dc2.blit(scr)
        bak.blit(scr)
        mc1.blit(scr)
        mc2.blit(scr)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                if hit_s.rct.collidepoint(event.pos):
                    m_hand = Hit(m_hand)
                    m_num = Return_sum(m_hand)
                elif std.rct.collidepoint(event.pos):
                    Judge(m_num, d_num, mwin, dwin, d_hand)

        if (mwin == 5) or (dwin == 5):
            return

        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()