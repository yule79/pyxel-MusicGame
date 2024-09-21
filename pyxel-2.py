from collections import deque, namedtuple

import pyxel
Point = namedtuple("Point", ["x", "y"])  # Convenience class for coordinates

COL_BACKGROUND = 3
COL_BODY = 11
COL_HEAD = 7
COL_DEATH = 5
COL_APPLE = 8

TEXT_DEATH = ["GAME OVER", "(Q)UIT", "(R)ESTART"]
COL_TEXT_DEATH = 0
HEIGHT_DEATH = 5

WIDTH = 40
HEIGHT = 50

HEIGHT_SCORE = pyxel.FONT_HEIGHT
COL_SCORE = 6
COL_SCORE_BACKGROUND = 5

UP = Point(0, -1)
DOWN = Point(0, 1)
RIGHT = Point(1, 0)
LEFT = Point(-1, 0)

START = Point(5, 5 + HEIGHT_SCORE)

y=0
y_2=160
y_3=160
yy=160
yy_2=160
yy_3=160
yyy=160
yyy_2=160
yyy_3=160
yyyy=160
yyyy_2=160
yyyy_3=160
timer=0
score=0
D_point_S=0
D_point_D=0
D_point_J=0
D_point_K=0
point_2=0
combo=0
combo_2=0
ys = [y,y_2,yy,yy_2,yyy,yyy_2,yyyy,yyyy_2]

class App:

    def __init__(self):
        pyxel.init(120, 120, title="Good Bye Sengen Key:S,D,J,K")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.bgm()
        self.o = 0
        pyxel.run(self.update,self.draw)
    def reset(self):
        self.death = False
        pyxel.playm(0, loop=False)
    def draw_score(self):
        global point_2,combo_2
        point_2 = f"{score:05}"
        pyxel.rect(0, 0, WIDTH, HEIGHT_SCORE, COL_SCORE_BACKGROUND)
        pyxel.text(1, 1, point_2, COL_SCORE)
        combo_2 = f"    S      D      J      K"
        pyxel.text(1, 110, combo_2, COL_DEATH)
    def update(self):
        global y,y_2,y_3,yy,yy_2,yy_3,yyy,yyy_2,yyy_3,yyyy,yyyy_2,yyyy_3,timer,ys
        y+=3
        y_2+=3
        y_3+=3
        yy+=3
        yy_2+=3
        yy_3+=3
        yyy+=3
        yyy_2+=3
        yyy_3+=3
        yyyy+=3
        yyyy_2+=3
        yyyy_3+=3
        if self.o == 0:
            self.o+=1
        elif pyxel.frame_count % 10 == 0:
            timer += 1
        






#ブロックのテレポート
        if timer==5:
            yyyy-=yyyy
        if timer==12:
            y-=y
        if timer==17:
            yyyy-=yyyy
        if timer==25:
            yy-=yy
        if timer==26:
            yyy-=yyy
#in
        if timer==31:
            y-=y
        if timer==34:
            yy-=yy
            yyy-=yyy
        if timer==39:
            yyyy-=yyyy
        if timer==44:
            yy-=yy
            yyy-=yyy
        if timer==46:
            y-=y
            yyyy-=yyyy
        if timer==48:
            yy-=yy
        if timer==50:
            yyy-=yyy
        if timer==51:
            yyyy-=yyyy
#a
        if timer==54:
            y-=y
        if timer==56:
            yy-=yy
        if timer==58:
            yyy-=yyy
        if timer==61:
            y-=y
        if timer==63:
            y_2-=y_2
        if timer==68:
            yyyy-=yyyy
        if timer==70:
            yyyy_2-=yyyy_2
        if timer==76:
            yy-=yy
        if timer==77:
            yy_2-=yy_2
        if timer==79:
            yyy-=yyy
        if timer==80:
            yyy_2-=yyy_2
        if timer==82:
            y-=y
        if timer==85:
            y_2-=y_2
            yyyy-=yyyy 
        if timer==90:
            y-=y
            yyyy_2-=yyyy_2
#sabi
        if timer==93:
            y_2-=y_2
        if timer==94:
            yy-=yy
        if timer==95:
            yyy-=yyy
        if timer==96:
            yyyy-=yyyy
#
        if timer==101:
            y-=y
        if timer==102:
            yy-=yy
        if timer==103:
            yy_2-=yy_2
        if timer==105:
            yyy-=yyy
        if timer==106:
            yyy_2-=yyy_2
#
        if timer==112:
            yyyy-=yyyy
        if timer==113:
            yyy-=yyy
        if timer==114:
            yyy_2-=yyy_2
        if timer==116:
            yy-=yy
        if timer==117:
            yy_2-=yy_2
#half
        if timer==130:
            y-=y
        if timer==131:
            yy-=yy
        if timer==132:
            yy_2-=yy_2
        if timer==135:
            yyy-=yyy
        if timer==136:
            yyy_2-=yyy_2
#
        if timer==143:
            yyyy-=yyyy
        if timer==144:
            yyy-=yyy
        if timer==145:
            yyy_2-=yyy_2
        if timer==148:
            yy-=yy
        if timer==149:
            yy_2-=yy_2
#
        if timer==150:
            yyyy-=yyyy
        if timer==151:
            yyy-=yyy
        if timer==152:
            yy-=yy
#
        if timer==155:
            y-=y
        if timer==156:
            yy_2-=yy_2
        if timer==157:
            yyy_2-=yyy_2
#
        if timer==162:
            yyyy-=yyyy
        if timer==163:
            yyy-=yyy
        if timer==164:
            yy-=yy
#
        if timer==170:
            y-=y
        if timer==171:
            yy_2-=yy_2
        if timer==172:
            yyy_2-=yyy_2
#
        if timer==177:
            y-=y
            yyyy-=yyyy
        if timer==179:
            yy-=yy
            yyy-=yyy
        if timer==181:
            y_2-=y_2
            yy_2-=yy_2
            yyy_2-=yyy_2
            yyyy_2-=yyyy_2
#2
        if timer==186:
            yyyy-=yyyy
        if timer==193:
            y-=y
        if timer==198:
            yyyy-=yyyy
        if timer==212:
            yy-=yy
        if timer==213:
            yyy-=yyy
#
        if timer==218:
            y-=y
        if timer==221:
            yy-=yy
            yyy-=yyy
        if timer==226:
            yyyy-=yyyy
        if timer==231:
            yy-=yy
            yyy-=yyy
        if timer==233:
            y-=y
            yyyy-=yyyy
        if timer==235:
            yy-=yy
        if timer==237:
            yyy-=yyy
        if timer==238:
            yyyy-=yyyy
#52
        if timer==241:
            y-=y
        if timer==243:
            yy-=yy
        if timer==245:
            yyy-=yyy
        if timer==248:
            y-=y
        if timer==250:
            y_2-=y_2
        if timer==255:
            yyyy-=yyyy
        if timer==257:
            yyyy_2-=yyyy_2
        if timer==263:
            yy-=yy
        if timer==264:
            yy_2-=yy_2
        if timer==266:
            yyy-=yyy
        if timer==267:
            yyy_2-=yyy_2
#
        if timer==269:
            y-=y
        if timer==271:
            yyyy-=yyyy
        if timer==273:
            yy-=yy
            yyy-=yyy
        if timer==275:
            yy_2-=yy_2
            yyy_2-=yyy_2
#
        if timer==283:
            y-=y
        if timer==285:
            yyyy-=yyyy
        if timer==294:
            yy-=yy
        if timer==300:
            yyy-=yyy
        if timer==306:
            y-=y
        if timer==307:
            yy-=yy
        if timer==308:
            yyy-=yyy
        if timer==309:
            y_2-=y_2
        if timer==316:
            yyyy-=yyyy
        if timer==317:
            yyy-=yyy
        if timer==330:
            y-=y
        if timer==332:
            y_2-=y_2
        if timer==340:
            yyyy-=yyyy
        if timer==341:
            yyy-=yyy
        if timer==342:
            yy-=yy
#
        if timer==345:
            y-=y
        if timer==346:
            y_2-=y_2
        if timer==347:
            yyy-=yyy
        if timer==349:
            yyyy-=yyyy
        if timer==351:
            y-=y
        if timer==352:
            y_2-=y_2
        if timer==353:
            yy-=yy
        if timer==354:
            yy_2-=yy_2
        if timer==355:
            yyy-=yyy
        if timer==356:
            yyy_2-=yyy_2
        if timer==358:
            yyyy-=yyyy
        if timer==360:
            yyyy_2-=yyyy_2
        if timer==363:
            y-=y
        if timer==367:
            yy-=yy
            yyy-=yyy
        if timer==368:
            yy_2-=yy_2
            yyy_2-=yyy_2
        if timer==369:
            y_2-=y_2
            yyyy_2-=yyyy_2
#sabi
        if timer==375:
            y_2-=y_2
        if timer==376:
            yy-=yy
        if timer==377:
            yyy-=yyy
        if timer==378:
            yyyy-=yyyy
#
        if timer==383:
            yyyy_2-=yyyy_2
        if timer==384:
            yyy_2-=yyy_2
        if timer==385:
            yyy-=yyy
        if timer==387:
            yy-=yy
        if timer==388:
            yy_2-=yy_2
#
        if timer==394:
            y-=y
        if timer==395:
            yy-=yy
        if timer==396:
            yy_2-=yy_2
        if timer==398:
            yyy-=yyy
        if timer==399:
            yyy_2-=yyy_2
#half
        if timer==412:
            yyyy-=yyyy
        if timer==413:
            yyy-=yyy
        if timer==414:
            yyy_2-=yyy_2
        if timer==416:
            yy-=yy
        if timer==417:
            yy_2-=yy_2
#
        if timer==423:
            y-=y
        if timer==424:
            yy-=yy
        if timer==425:
            yy_2-=yy_2
        if timer==427:
            yyy-=yyy
        if timer==428:
            yyy_2-=yyy_2
#
        if timer==434:
            y-=y
            yyyy_2-=yyyy_2
        if timer==435:
            yy_2-=yy_2
            yyy_2-=yyy_2
        if timer==436:
            y_2-=y_2
            yyyy-=yyyy
#
        if timer==438:
            y-=y
            yyyy_2-=yyyy_2
        if timer==441:
            y_2-=y_2
            yyyy-=yyyy
        if timer==445:
            y-=y
            yyyy_2-=yyyy_2
        if timer==448:
            y_2-=y_2
            yyyy_3-=yyyy_3
#
        if timer==461:
            y_3-=y_3
            yyyy-=yyyy
        if timer==463:
            yy_3-=yy_3
            yyy_3-=yyy_3
        if timer==465:
            yyyy_3-=yyyy_3





        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
    def bgm(self):
        pyxel.playm(0,loop=False)
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 120, 160)

        pyxel.blt(10, y, 1, 0, 0, 120, 160, 0)
        pyxel.blt(10, y_2, 1, 0, 0, 120, 160, 0)
        pyxel.blt(10, y_3, 1, 0, 0, 120, 160, 0)
        pyxel.blt(37, yy, 1, 0, 0, 120, 160, 0)
        pyxel.blt(37, yy_2, 1, 0, 0, 120, 160, 0)
        pyxel.blt(37, yy_3, 1, 0, 0, 120, 160, 0)
        pyxel.blt(65, yyy, 1, 0, 0, 120, 160, 0)
        pyxel.blt(65, yyy_2, 1, 0, 0, 120, 160, 0)
        pyxel.blt(65, yyy_3, 1, 0, 0, 120, 160, 0)
        pyxel.blt(93, yyyy, 1, 0, 0, 120, 160, 0)
        pyxel.blt(93, yyyy_2, 1, 0, 0, 120, 160, 0)
        pyxel.blt(93, yyyy_3, 1, 0, 0, 120, 160, 0)

        if pyxel.btn(pyxel.KEY_S):
            pyxel.blt(10, 100, 2, 0, 0, 120, 160, 0)
            self.check_death(0)
            
        if pyxel.btn(pyxel.KEY_D):
            pyxel.blt(37, 100, 2, 0, 0, 120, 160, 0)
            self.check_death(1)
            
        if pyxel.btn(pyxel.KEY_J):
            pyxel.blt(65, 100, 2, 0, 0, 120, 160, 0)
            self.check_death(2)
            
        if pyxel.btn(pyxel.KEY_K):
            pyxel.blt(93, 100, 2, 0, 0, 120, 160, 0)
            self.check_death(3)
        self.draw_score()
    def check_death(self,key_num):
        global score
        if key_num==0 and 90<=y<=110 or 90<=y_2<=110 or 90<=y_3<=110:
                score+=1
        elif key_num==0 and 95<=y<=105 or 95<=y_2<=105 or 95<=y_3<=105:
                score+=1
        elif key_num==1 and 90<=yy<=110 or 90<=yy_2<=110 or 90<=yy_3<=110:
                score+=1
        elif key_num==1 and 95<=yy<=105 or 95<=yy_2<=105 or 95<=yy_3<=105:
                score+=1
        elif key_num==2 and 90<=yyy<=110 or 90<=yyy_2<=110 or 90<=yyy_3<=110:
                score+=1
        elif key_num==2 and 95<=yyy<=105 or 95<=yyy_2<=105 or 95<=yyy_3<=105:
                score+=1
        elif key_num==3 and 90<=yyyy<=110 or 90<=yyyy_2<=110 or 90<=yyyy_3<=110:
                score+=1
        elif key_num==3 and 95<=yyyy<=105 or 95<=yyyy_2<=105 or 95<=yyyy_3<=105:
                score+=1

                
    def draw_death(self):
        pyxel.cls(col=COL_DEATH)
        display_text = TEXT_DEATH[:]
        display_text.insert(1, f"{self.score:04}")
        for i, text in enumerate(display_text):
            y_offset = (pyxel.FONT_HEIGHT + 2) * i
            text_x = self.center_text(text, WIDTH)
            pyxel.text(text_x, HEIGHT_DEATH + y_offset, text, COL_TEXT_DEATH)
    @staticmethod
    def center_text(text, page_width, char_width=pyxel.FONT_WIDTH):
        text_width = len(text) * char_width
        return (page_width - text_width) // 2
App()