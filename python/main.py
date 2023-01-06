import pygame
from tools import *
import datetime

pygame.init()
screen = pygame.display.set_mode([500, 900])
pygame.display.set_caption("阳光农场")
scene = 1
bar = False
font_name2 = pygame.font.match_font('kaiti')
font2 = pygame.font.Font(font_name2, 20)
tian = None
clock = pygame.time.Clock()
running = True
time = 0
tian_i = [0, 0, 0, 0, 0, 0, 0, 0, 0]
next_click_time = 0.0
times = []
lens = 0
sh = False
timu = False
hours = 0
minute = 0
answers = shengcheng_timu()
xxx = None
yyy = False
while running:
    clock.tick(30)
    time += 0.02
    if time % 1 >= 0.6:
        for i in range(9):
            if tian_coollect[i] == -1:
                break
            if now[i] == 0 or now[i] == 1:
                continue
            tian_coollect[i] += tian_poses[i][tian_i[i]]
        time = 1
    if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute == 0 and \
            datetime.datetime.now().second == 0:
        answers = shengcheng_timu()
        hours = 0
        wc = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 400 <= x <= 500 and 840 <= y <= 900:
                sh = True
        if event.type == pygame.MOUSEBUTTONDOWN and sh:
            x, y = pygame.mouse.get_pos()
            if sh:
                if 25 + 327 <= x <= 25+425 and y+127 <= y <= y+169 and sh:
                    sh = False
                if 327+25 <= x <= 327+25+100 and 127 + 75 <= y <= 127+75+60 and sh and wc[0] == 0:
                    sunlight += 20
                    wc[0] = 1
                if 327 + 25 <= x <= 327 + 25 + 100 and 127 + 75+220 <= y <= 127 + 75 + 60+220 and sh and wc[1] == 0:
                    wc[1] = 1
                    timu = True
                if 0 <= x <= 500 and 0 <= y <= 50:
                    sh = False
        if event.type == pygame.MOUSEBUTTONDOWN and timu:
            x, y = pygame.mouse.get_pos()
            if 25 <= x <= 225:
                if 125 <= y <= 125+60:
                    xxx = "A"
                if 125+60 <= y <= 125+60*2:
                    xxx = "B"
                if 125+120 <= y <= 125+60*3:
                    xxx = "C"
                if 125+180 <= y <= 125+60*4:
                    xxx = "D"
            if (0 <= x <= 500 and 0 <= y <= 50) or (0 <= x <= 500 and 810 <= y <= 900):
                timu = False
        if scene == 1:
            for i in range(9):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    times.append([[x, y], time - next_click_time])
                    lens += 1
                    next_click_time = time
                    flag = 0
                    if pos[i][0] <= x <= pos[i][0]+170 and pos[i][1] <= y <= pos[i][1]+170:
                        if pos[i][0]+130 <= x <= pos[i][0]+160 and pos[i][1]+140 <= y <= pos[i][1]+160:
                            flag = 1
                            bar = True
                            tian = i+1
                        if sunlight >= tian_money[i] and now[i] == 1:
                            sunlight -= tian_money[i]
                            now[i] = 0
                            tian_coollect[i] = 0
                        elif now[i] == 0:
                            bar = True
                            tian = i+1
                        else:
                            if tian_coollect[i] != -1:
                                guan += tian_coollect[i]
                                tian_coollect[i] = 0
                                if tongguan_shuliang[now_guan] <= guan:
                                    guan -= tongguan_shuliang[now_guan]
                                    now_guan += 1
                                    sunlight += 15
        if bar:
            for i in range(1, 4, 1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    y = 75
                    for x in range(i - 1):
                        y += 220 + 25
                    f, g = pygame.mouse.get_pos()
                    times.append([[f, g], time-next_click_time])
                    lens += 1
                    next_click_time = time
                    if 25 + 327 <= f <= 25+425 and y+127 <= g <= y+169 and not sh:
                        if now_guan >= zuowu_lock[tian-1][i-1]:
                            bar = False
                            now[tian-1] = "caidi-"+str(tian)+"_"+str(i)+".jpg"
                            tian_i[tian-1] = i-1
                        else:
                            print("没有达到此等级！")
                            bar = False
            if bar:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    times.append([[x, y], time - next_click_time])
                    lens += 1
                    next_click_time = time
                    if (0 <= x <= 500 and 0 <= y <= 50) or (0 <= x <= 500 and 810 <= y <= 900):
                        bar = False
    screen.fill([255, 255, 255])
    if scene == 1:
        screen.blit(pygame.image.load("./images/shengchan.jpg"), [0, 0])
        screen.blit(pygame.image.load("./images/sunlight.jpg"), [250, 0])
        font_surface = font2.render(str(sunlight), True, 'orange')
        screen.blit(font_surface, [300, 15])
        font_surface = font2.render(str(tongguan_shuliang[now_guan]) + "/" + str(int(guan)), True, 'orange')
        screen.blit(font_surface, [50, 12])
        font_surface = font2.render(str(now_guan), True, 'orange')
        screen.blit(font_surface, [25, 12.5])
        screen.blit(pygame.image.load("./images/shop.jpg"), [400, 840])
        for i in range(9):
            if now[i] == 0:
                screen.blit(pygame.image.load("./images/blank.jpg"), pos[i])
            elif now[i] == 1:
                screen.blit(pygame.image.load("./images/locked.jpg"), pos[i])
                font_surface = font2.render(str(tian_money[i]), True, 'green')
                screen.blit(font_surface, tm_pos[i])
            else:
                screen.blit(pygame.image.load("./images/" + now[i]), pos[i])
        for i in range(9):
            if tian_coollect[i] > 0 and now[i] != 0 and now[i] != 1:
                font_surface = font2.render(str(int(tian_coollect[i])), True, 'red')
                screen.blit(font_surface, [pos[i][0] + 75, pos[i][1] - 10])
        if bar:
            screen.blit(pygame.image.load("./images/renwu.jpg"), [0, 50])
            for i in range(1, 4, 1):
                y = 75
                for x in range(i-1):
                    y += 220 + 25
                screen.blit(pygame.image.load("./images/card.jpg"), [25, y])
                screen.blit(pygame.image.load("./images/caidi-" + str(tian) + "_" + str(i) + ".jpg"), [55, y+25])
                font_surface = font2.render("解锁等级：" + str(zuowu_lock[tian-1][i-1]), True, 'blue')
                screen.blit(font_surface, [250, y+80])
        if sh:
            screen.blit(pygame.image.load("./images/renwu.jpg"), [0, 50])
            screen.blit(pygame.image.load("./images/card.jpg"), [25, 75])
            if wc[0] == 0:
                screen.blit(pygame.image.load("./images/yg.jpg"), [327+25, 127+75])
                font_surface = font2.render("去完成", True, 'black')
                screen.blit(font_surface, [340+30, 135+87])
            else:
                screen.blit(pygame.image.load("./images/ygm.jpg"), [327+25, 127+75])
                font_surface = font2.render("已完成", True, 'black')
                screen.blit(font_surface, [340+30, 135+87])
            font_surface = font2.render(renwu[0], True, 'black')
            screen.blit(font_surface, [40, 100])
            screen.blit(pygame.image.load("./images/card.jpg"), [25, 320])
            if wc[1] == 0:
                screen.blit(pygame.image.load("./images/yg.jpg"), [327 + 25, 127 + 320])
                font_surface = font2.render("去完成", True, 'black')
                screen.blit(font_surface, [340 + 30, 135 + 87+220+25])
            else:
                screen.blit(pygame.image.load("./images/ygm.jpg"), [327 + 25, 127 + 320])
                font_surface = font2.render("已完成", True, 'black')
                screen.blit(font_surface, [340 + 30, 135 + 87+220+25])
            font_surface = font2.render(renwu[1], True, 'black')
            screen.blit(font_surface, [40, 360])
        if timu and xxx is None:
            screen.blit(pygame.image.load("./images/renwu.jpg"), [0, 50])
            font_surface = font2.render(answers[0], True, 'black')
            screen.blit(font_surface, [25, 75])
            screen.blit(pygame.image.load("./images/timu.jpg"), [25, 125])
            screen.blit(pygame.image.load("./images/timu.jpg"), [25, 125+60])
            screen.blit(pygame.image.load("./images/timu.jpg"), [25, 125+120])
            screen.blit(pygame.image.load("./images/timu.jpg"), [25, 125+180])
            screen.blit(font2.render(answers[1], True, 'black'), [50, 150])
            screen.blit(font2.render(answers[2], True, 'black'), [50, 150+60])
            screen.blit(font2.render(answers[3], True, 'black'), [50, 150+60*2])
            screen.blit(font2.render(answers[4], True, 'black'), [50, 150+180])
        if timu and xxx is not None:
            screen.blit(pygame.image.load("./images/renwu.jpg"), [0, 50])
            font_surface = font2.render(answers[0], True, 'black')
            screen.blit(font_surface, [25, 75])
            if xxx != answers[5]:
                yyy = True
            if yyy:
                if xxx == "A":
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125])
                elif answers[5] == "A":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125])
                if xxx == "B":
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+60])
                elif answers[5] == "B":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+60])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+120-60])
                if xxx == "C":
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+120])
                elif answers[5] == "C":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+120])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+120])
                if xxx == "D":
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+180])
                elif answers[5] == "D":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+180])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+180])
            else:
                sunlight += 30
                if xxx == "A":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125])
                if xxx == "B":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+60])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+60])
                if xxx == "C":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+120])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+120])
                if xxx == "D":
                    screen.blit(pygame.image.load("./images/yes.jpg"), [25, 125+180])
                else:
                    screen.blit(pygame.image.load("./images/no.jpg"), [25, 125+180])
            screen.blit(font2.render(answers[1], True, 'black'), [50, 150])
            screen.blit(font2.render(answers[2], True, 'black'), [50, 150+60])
            screen.blit(font2.render(answers[3], True, 'black'), [50, 150+60*2])
            screen.blit(font2.render(answers[4], True, 'black'), [50, 150+180])
            timu = False
    pygame.display.flip()
pygame.quit()
