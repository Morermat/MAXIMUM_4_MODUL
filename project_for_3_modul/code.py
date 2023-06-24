from tkinter import *
from pygame import mixer,init,time
import random
import math
from PIL import Image, ImageTk

win = Tk()

w = 640
h = 480
phaseperemenayaultimatecodeversion=0
tikscore=0

srpites=[[PhotoImage(file=f'file//jevil//avatar{i}.png')for i in range(1,15)],
         PhotoImage(file='file\\menu backround\\bg.png'),
         PhotoImage(file='file\\HUD\\textbox.png'),
         PhotoImage(file='file\\game over\\gameover.png'),
         PhotoImage(file='file\\jevil\\bird.png')
    ]
battleboxsprites=[[PhotoImage(file=f'file//battle box//Frames//e000{i}.png')for i in range(7,10)],
                  [PhotoImage(file=f'file//battle box//Frames//e00{i}.png')for i in range(10,64)],
                  ]
width_new = win.winfo_screenwidth()
height_new = win.winfo_screenheight()
win.geometry(str(w) + 'x' + str(h)+'+'+str(int((win.winfo_screenwidth()-w)/2))+'+'+str(int((win.winfo_screenheight()-h)/2)))
win.resizable(width=False, height=False)
win.title('DELTARUNE')
win.iconbitmap('file\\title logo\\logo.ico')
canvas = Canvas(win, width=width_new, height=height_new)
canvas.place(in_=win, x=0, y=0)
mixer.init()
mixer.set_num_channels(10)
class Soul:
    def __init__(self):
        self.x=0
        self.y=0
        self.v=1
        self.v1=1
        self.spr=[[PhotoImage(file=f'file\\red soul\\soulcrush{i}.png') for i in range(1,8)],
                  PhotoImage(file='file\\red soul\\soul.png'),
                  PhotoImage(file='file\\red soul\\soulpn.png')
                  ]
class Attacks:
    def __init__(self,x,y,rota):
        self.x=x
        self.y=y
        self.syrclefalltickscore=0
        self.rota=rota
        self.syrclefallprozrachnost=255
        self.spr=[[Image.open(f'file\\jevil\\attack{i}.png') for i in range(1,10)],
                  [Image.open(f'file\\jevil\\attackflash{i}.png') for i in range(11,19)],
                  Image.open('file\\jevil\\syrcle.png').convert('RGBA')
                  ]
        self.useimage1=self.spr[2].rotate(self.rota)
        self.useimage=useimage=ImageTk.PhotoImage(self.useimage1)
    def crateimage(self,can):
        can.create_image(int(self.x),int(self.y),image=self.useimage)
    def changeygol(self):
        self.rota-=-1.8
        self.useimage1=self.spr[2].rotate(int(self.rota))
        self.useimage=ImageTk.PhotoImage(self.useimage1)
class Jevil:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xc=320
        self.yc=240
        self.xb=320
        self.yb=240
        self.avatarbytelist=0
        self.avatartiskscorelist=0
        self.spt=[[PhotoImage(file=f'file//jevil//avatar{i}.png')for i in range(1,15)],
             PhotoImage(file=f'file//jevil//bg.png')]
        self.usetext=''
        self.fulltext=['* УИ-И ХИ-И!    \n* ПОСЕТИТЕЛИ, ПОСЕТИТЕЛИ!    \n* ТЕПЕРЬ МЫ МОЖЕМ ИГРАТЬ, ИГРАТЬ!',
                       '* А ПОСЛЕ ВАС Я СМОГУ ПОИГРАТЬ    \n  И СО ВСЕМИ ОСТАЛЬНЫМИ!',
                       '* Так а во что мы    \n  играем?..',
                       '* О, ЭТО ПРОСТАЯ ИГРА С ЧИСЛАМИ.',
                       '* ЕСЛИ ВАШИ ОЗ УПАДУТ ДО 0,    \n  ВЫ ПРОИГРАЛИ!',
                       '* Так вот в какие игры ты    \n  хочешь играть, да?..',
                       '* Тогда, мне надо тебя    \n  предупредить...',
                       '* Ты имеешь дело с    \n  парочкой акул.','',
                       '* УИ-И ХИ-И ХИ-И! УКУСОМ НА УКУС!    \n  ДРУГОГО Я И НЕ ОЖИДАЛ!',
                       '* А ТЕПЕРЬ, А ТЕПЕРЬ!!    \n* НАЧНЁМ ЖЕ ИГРАТЬ!!'
                       ]
        self.textuselustbyte=0
        self.textusebyte=0
        self.texttickscorebyte=0
        self.spr=[[PhotoImage(file=f'file\\jevil\\main{i}.png') for i in range(1,4)],
                  [PhotoImage(file=f'file\\jevil\\frontl{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\jevil\\frontr{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\jevil\\hurt{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\jevil\\tp{i}.png') for i in range(1,5)],
                  PhotoImage(file='file\\ralsei\\ralseitalk.png'),
                  [PhotoImage(file=f'file\\susie\\susietext{i}.png') for i in range(1,4)]
                  ]
        self.useimagebyte=0
        self.useimage=self.spr[0][self.useimagebyte]
        self.mainimagetickscorebyte=0
    def createimage(self,can):
        can.create_image(self.x,self.y,image=self.useimage)
    def changetext(self):
        if self.textuselustbyte==2:
            if self.textusebyte+1<=len(self.fulltext[self.textuselustbyte]):
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!=' ' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!='*' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    sound=mixer.Sound("file\\mus\\snd_txtral_ch1.wav")
                    sound.play()
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    self.usetext=self.fulltext[self.textuselustbyte][0:self.textusebyte]
                self.textusebyte+=1
        elif self.textuselustbyte==5 or self.textuselustbyte==6 or self.textuselustbyte==7:
            if self.textusebyte+1<=len(self.fulltext[self.textuselustbyte]):
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!=' ' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!='*' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    sound=mixer.Sound("file\\mus\\snd_txtsus_ch1.wav")
                    sound.play()
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    self.usetext=self.fulltext[self.textuselustbyte][0:self.textusebyte]
                self.textusebyte+=1
        else:
            if self.textusebyte+1<=len(self.fulltext[self.textuselustbyte]):
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!=' ' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+1]!='*' and self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    sound=mixer.Sound("file\\mus\\snd_txtjok_ch1.wav")
                    sound.play()
                if self.fulltext[self.textuselustbyte][self.textusebyte:self.textusebyte+2]!='\n':
                    self.usetext=self.fulltext[self.textuselustbyte][0:self.textusebyte]
                self.textusebyte+=1
    def createtext(self,can,spr):
        if self.textuselustbyte==2:
            can.create_image(320,397,image=spr[2])
            can.create_image(50,340,image=self.spr[5],anchor="nw")
            can.create_text(156,340,text=self.usetext,font='Arial 20',fill="#FFFFFF",anchor="nw")
        elif self.textuselustbyte==5 or self.textuselustbyte==6 or self.textuselustbyte==7:
            can.create_image(320,397,image=spr[2])
            if self.textuselustbyte==5:
                can.create_image(50,340,image=self.spr[6][0],anchor="nw")
            if self.textuselustbyte==6:
                can.create_image(50,340,image=self.spr[6][1],anchor="nw")
            if self.textuselustbyte==7:
                can.create_image(50,340,image=self.spr[6][2],anchor="nw")
            can.create_text(156,340,text=self.usetext,font='Arial 20',fill="#FFFFFF",anchor="nw")
        else:
            can.create_image(320,397,image=spr[2])
            can.create_text(50,340,text=self.usetext,font='Arial 20',fill="#FFFFFF",anchor="nw")
    def changemainimage(self):
        self.mainimagetickscorebyte+=1
        if self.mainimagetickscorebyte==20:
            self.mainimagetickscorebyte=0
            if self.useimagebyte==1:
                self.useimagebyte=0
            else:
                self.useimagebyte+=1
            self.useimage=self.spr[0][self.useimagebyte]
    def createimagebg(self,can):
        if self.xb>560 and self.xb<=1200:
            can.create_image(int(self.xb),int(self.yb),image=self.spt[1])
            can.create_image(int(self.xb-1120),int(self.yb),image=self.spt[1])
            can.create_rectangle(0,240,640,480,fill='black')
            can.create_image(int(self.xc),int(self.yc),image=self.spt[0][self.avatarbytelist])
        elif self.xb<=560:
            can.create_image(int(self.xb),int(self.yb),image=self.spt[1])
            can.create_rectangle(0,240,640,480,fill='black')
            can.create_image(int(self.xc),int(self.yc),image=self.spt[0][self.avatarbytelist])
        elif self.xb>1200:
            self.xb-=1120
            can.create_image(int(self.xb),int(self.yb),image=self.spt[1])
            can.create_rectangle(0,240,640,480,fill='black')
            can.create_image(int(self.xc),int(self.yc),image=self.spt[0][self.avatarbytelist])
        self.xb+=1
        if self.avatartiskscorelist>=40:
            self.avatarbytelist+=1
            if self.avatarbytelist>13:
                self.avatarbytelist=0
            self.avatartiskscorelist=0
        self.avatartiskscorelist+=5
class Kris:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.spr=[[PhotoImage(file=f'file\\kris\\kris{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\kris\\krisact{i}.png') for i in range(1,14)],
                  [PhotoImage(file=f'file\\kris\\krisafterbattle{i}.png') for i in range(1,10)],
                  [PhotoImage(file=f'file\\kris\\krisattack{i}.png') for i in range(1,10)],
                  [PhotoImage(file=f'file\\kris\\krisbattle{i}.png') for i in range(1,13)],
                  [PhotoImage(file=f'file\\kris\\krisitem{i}.png') for i in range(1,9)],
                  [PhotoImage(file=f'file\\kris\\krisshield{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\kris\\krisspin{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\kris\\krisstay{i}.png') for i in range(1,7)],
                  PhotoImage(file=f'file\\kris\\krisfall.png')
                  ]
        self.useimage=self.spr[0][0]
        self.spritephase=0
        self.tickscore=0
        self.attackphasestop=0
    def createimage(self,can):
        can.create_image(int(self.x),int(self.y),image=self.useimage)
    def walk(self,newx):
        self.spritephase+=1
        if self.spritephase==4:
            self.spritephase=0
        self.useimage=self.spr[0][self.spritephase]
    def changeimage(self,mode):
        if mode=='AttackOne':
            if self.spritephase>=8:
                self.spritephase=8
                self.attackphasestop=1
            else:
                self.spritephase+=1
            self.useimage=self.spr[3][self.spritephase]
        elif mode=='Prebattle':
            if self.spritephase>=11:
                self.spritephase=11
                self.attackphasestop=1
            else:
                self.spritephase+=1
            self.useimage=self.spr[4][self.spritephase]
class Susie:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.spr=[[PhotoImage(file=f'file\\susie\\susie{i}.png') for i in range(11,15)],
                  [PhotoImage(file=f'file\\susie\\susie{i}.png') for i in range(21,25)],
                  [PhotoImage(file=f'file\\susie\\rudebuster{i}.png') for i in range(1,8)],
                  [PhotoImage(file=f'file\\susie\\susieact{i}.png') for i in range(1,12)],
                  [PhotoImage(file=f'file\\susie\\susieafterbettle{i}.png') for i in range(1,21)],
                  [PhotoImage(file=f'file\\susie\\susieattack{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\susie\\susiedefense{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\susie\\susiefall{i}.png') for i in range(1,3)],
                  [PhotoImage(file=f'file\\susie\\susiepreattack{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\susie\\susieprerudebuster{i}.png') for i in range(1,10)],
                  [PhotoImage(file=f'file\\susie\\susierudebuster{i}.png') for i in range(1,16)],
                  [PhotoImage(file=f'file\\susie\\susiestay{i}.png') for i in range(1,5)],'',
                  [PhotoImage(file=f'file\\susie\\susieuse{i}.png') for i in range(1,8)],
                  PhotoImage(file='file\\susie\\susieshock.png')
                  ]
        self.useimage=self.spr[0][0]
        self.spritephase=0
        self.tickscore=0
        self.attackphasestop=0
    def createimage(self,can):
        can.create_image(int(self.x),int(self.y),image=self.useimage)
    def walk(self,newx):
        self.spritephase+=1
        if self.spritephase==4:
            self.spritephase=0
        self.useimage=self.spr[0][self.spritephase]
    def changeimage(self,mode):
        if mode=='AttackOne':
            if self.spritephase>=5:
                self.spritephase=5
            else:
                self.spritephase+=1
            self.useimage=self.spr[5][self.spritephase]
        elif mode=='Prebattle':
            if self.spritephase>=5:
                self.spritephase=5
            else:
                self.spritephase+=1
            self.useimage=self.spr[5][self.spritephase]
class Ralsei:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.spr=[[PhotoImage(file=f'file\\ralsei\\ralsei{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiact{i}.png') for i in range(1,11)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiafterbattle{i}.png') for i in range(1,14)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiattack{i}.png') for i in range(1,8)],
                  [PhotoImage(file=f'file\\ralsei\\ralseidefense{i}.png') for i in range(1,7)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiitem{i}.png') for i in range(1,10)],
                  [PhotoImage(file=f'file\\ralsei\\ralseimagic{i}.png') for i in range(1,5)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiprebattle{i}.png') for i in range(1,10)],
                  [PhotoImage(file=f'file\\ralsei\\ralseistay{i}.png') for i in range(1,6)],
                  [PhotoImage(file=f'file\\ralsei\\ralseiusemagic{i}.png') for i in range(1,11)],
                  PhotoImage(file='file\\ralsei\\ralseifall.png'),
                  PhotoImage(file='file\\ralsei\\ralseishock.png'),
                  ]
        self.useimage=self.spr[0][0]
        self.spritephase=0
        self.tickscore=0
    def createimage(self,can):
        can.create_image(int(self.x),int(self.y),image=self.useimage)
    def walk(self,newx):
        self.spritephase+=1
        if self.spritephase==4:
            self.spritephase=0
        self.useimage=self.spr[0][self.spritephase]
    def changeimage(self,mode):
        if mode=='AttackOne':
            if self.spritephase>=6:
                self.spritephase=6
            else:
                self.spritephase+=1
            self.useimage=self.spr[3][self.spritephase]
        elif mode=='Prebattle':
            if self.spritephase>=8:
                self.spritephase=8
            else:
                self.spritephase+=1
            self.useimage=self.spr[7][self.spritephase]
class Bindbutton:
    def __init__(self):
        self.upi=0
        self.downi=0
        self.lefti=0
        self.righti=0
        self.confirmi=0
        self.canceli=0
    def up(self,event):
        self.upi=1
    def down(self,event):
        self.downi=1
    def left(self,event):
        self.lefti=1
    def right(self,event):
        self.righti=1
    def confirmdef(self):
        self.confirmi=1
    def cancel(self):
        self.canceli=1
    def stop(self,event):
        if event.keycode==38:
            self.upi=0
        if event.keycode==40:
            self.downi=0
        if event.keycode==37:
            self.lefti=0
        if event.keycode==39:
            self.righti=0
        if event.keycode==90:
            self.confirmi=0
        if event.keycode==88:
            self.canceli=0
    def choisebutton(self,event):
        if event.keycode==88:
            self.cancel()
        if event.keycode==90:
            self.confirmdef()
#=============================================Расположение============================================
def xcoodrinate(xitem,yitem,xplace,yplace,vitem):
    newxitem=((xplace-xitem)/(((((yplace-yitem)**2)+((xplace-xitem)**2))**(0.5))/vitem))*5
    return newxitem
def ycoodrinate(xitem,yitem,xplace,yplace,vitem):
    newyitem=((yplace-yitem)/((((yplace-yitem)**2+(xplace-xitem)**2)**(0.5))/vitem))*5
    return newyitem
def get_r_xcoordinate(radius,ygol):
    return radius*math.sin(ygol/57.3)
def get_r_ycoordinate(radius,ygol):
    return radius*math.cos(ygol/57.3)
def get_ygol(xi,yi,xp,yp):
    if yp-yi>=0:
        return 180-(math.asin((xp-xi)/(((xp-xi)**2+(yp-yi)**2)**(0.5)))*57.3)
    if yp-yi<0:
        if xp-xi>=0:
            return 180-(math.acos((yp-yi)/(((xp-xi)**2+(math.fabs(yp-yi)**2))**(0.5)))*57.3)
        if xp-xi<0:
            return 180+(math.acos((yp-yi)/(((math.fabs(xp-xi))**2+(math.fabs(yp-yi)**2))**(0.5)))*57.3)
#=================================================RGB=================================================
def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb 
#=================================================Игра================================================
def game():
    global phaseperemenayaultimatecodeversion,sound1,tikscore,srpites,scyresfall,scyresfallyglobal,scyresfalltickscore,soundlaught
    canvas.delete('all')
    if phaseperemenayaultimatecodeversion==0:
        mixer.music.load("file\\mus\\AUDIO_STORY.mp3")
        mixer.music.play(loops=-1, start=0.0, fade_ms = 0)
        phaseperemenayaultimatecodeversion=1
    if phaseperemenayaultimatecodeversion==1:
        canvas.create_image(320,240, image=srpites[1])
        canvas.create_rectangle(110,110,540,375,fill='black',stipple='gray75',outline='#FFFFFF')
        canvas.create_text(320, 240, text= "\nМы можем начать.       \n\n\n\n\nZ/Я-Подтвердить\nX/Ч-Отмена\nСтрелки-перемещение\n",fill="white",font=('Helvetica 15 bold'))
        if bindbutton.confirmi==1:
            phaseperemenayaultimatecodeversion=2
            bindbutton.confirmi=0
            mixer.music.load("file\\mus\\prejoker.mp3")
            mixer.music.play(loops=-1, start=0.0, fade_ms = 0)
            kris.tickscore=tikscore
    if phaseperemenayaultimatecodeversion==2:
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        jevil.createimage(canvas)
        kris.createimage(canvas)
        susie.createimage(canvas)
        ralsei.createimage(canvas)
        if tikscore-kris.tickscore>=175:
            kris.tickscore=tikscore
            kris.walk(5)
            susie.walk(5)
            ralsei.walk(5)
        kris.x+=0.25
        susie.x+=0.25
        ralsei.x+=0.25
        if kris.x>=175:
            phaseperemenayaultimatecodeversion=3
            susie.useimage=susie.spr[0][0]
            kris.useimage=kris.spr[0][0]
            ralsei.useimage=ralsei.spr[0][0]
            sound44=mixer.Sound("file\\mus\\snd_joker_laugh1_ch1.wav")
            sound44.play()
    if phaseperemenayaultimatecodeversion==3:
        if bindbutton.confirmi==1:
            bindbutton.confirmi=0
            jevil.textuselustbyte+=1
            jevil.textusebyte=0
            jevil.texttickscorebyte=0
        if jevil.textuselustbyte==4:
            phaseperemenayaultimatecodeversion=4
            scyresfall=[Attacks(200,-150,0),Attacks(200,-50,0)]
            scyresfalltickscore=0
            sound=mixer.Sound("file\\mus\\snd_joker_ha0_ch1.wav")
            susie.useimage=susie.spr[14]
            ralsei.useimage=ralsei.spr[11]
            sound.play()
            sound1=mixer.Sound("file\\mus\\snd_scytheburst_ch1.wav")
            sound1.play()
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        jevil.createtext(canvas,srpites)
        if jevil.texttickscorebyte==35:
            jevil.texttickscorebyte=0
            jevil.changetext()
        jevil.texttickscorebyte+=5
    if phaseperemenayaultimatecodeversion==4:
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        jevil.changemainimage()
        for i in scyresfall:
            i.y+=4
            i.changeygol()
            i.crateimage(canvas)
        if kris.x>100:
            kris.x-=1
            susie.x-=1
            ralsei.x-=1
        if scyresfall[0].y>=700:
            phaseperemenayaultimatecodeversion=5
            susie.useimage=susie.spr[1][0]
            kris.useimage=kris.spr[0][0]
            ralsei.useimage=ralsei.spr[0][0]
            jevil.useimage=jevil.spr[0][0]
    if phaseperemenayaultimatecodeversion==5:
        if bindbutton.confirmi==1:
            bindbutton.confirmi=0
            jevil.textuselustbyte+=1
            jevil.textusebyte=0
            jevil.texttickscorebyte=0
        if jevil.textuselustbyte==7:
            sound1.play
            phaseperemenayaultimatecodeversion=6
            kris.spritephase=0
            susie.spritephase=0
            ralsei.spritephase=0
            kris.tickscore=0
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        jevil.createtext(canvas,srpites)
        if jevil.texttickscorebyte==35:
            jevil.texttickscorebyte=0
            jevil.changetext()
        jevil.texttickscorebyte+=5
    if phaseperemenayaultimatecodeversion==6:
        if kris.attackphasestop==1:
            kris.attackphasestop=0
            kris.tickscore=0
            soundlaught=mixer.Sound("file\\mus\\snd_joker_laugh0_ch1.wav")
            phaseperemenayaultimatecodeversion=7
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        if tikscore-kris.tickscore>=100:
            kris.tickscore=tikscore
            kris.changeimage('AttackOne')
            susie.changeimage('AttackOne')
            ralsei.changeimage('AttackOne')
    if phaseperemenayaultimatecodeversion==7:
        if bindbutton.confirmi==1:
            bindbutton.confirmi=0
            jevil.textuselustbyte+=1
            jevil.textusebyte=0
            jevil.texttickscorebyte=0
        if jevil.textuselustbyte==8:
            jevil.textuselustbyte+=1
            soundlaught.play(loops=-1)
        if jevil.textuselustbyte==11:
            phaseperemenayaultimatecodeversion=8
            jevil.useimage=jevil.spr[0][0]
            soundlaught.stop()
            mixer.music.load("file\\mus\\Wind.mp3")
            mixer.music.play(loops=-1, start=0.0, fade_ms = 0)
            soundprebattle=mixer.Sound("file\\mus\\snd_weaponpull_fast_ch1.wav")
            soundprebattle.play()
        if jevil.textuselustbyte>=9:
                jevil.changemainimage()
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        jevil.createtext(canvas,srpites)
        if jevil.texttickscorebyte==35:
            jevil.texttickscorebyte=0
            jevil.changetext()
        jevil.texttickscorebyte+=5
    if phaseperemenayaultimatecodeversion==8:
        if jevil.x>=555:
            phaseperemenayaultimatecodeversion='menu'
            mixer.music.load("file\\mus\\joker.mp3")
            mixer.music.play(loops=-1, start=0.0, fade_ms = 0)
        canvas.create_rectangle(0,0,640,480,fill='black')
        canvas.create_image(320,240, image=srpites[0][1])
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
        jevil.x+=xcoodrinate(jevil.x,jevil.y,560,240,0.5)
        jevil.y+=ycoodrinate(jevil.x,jevil.y,560,240,0.5)
        if tikscore-kris.tickscore>=300:
            kris.tickscore=tikscore
            kris.changeimage('Prebattle')
            susie.changeimage('Prebattle')
            ralsei.changeimage('Prebattle')
    if phaseperemenayaultimatecodeversion=='menu':
        jevil.createimagebg(canvas)
        kris.createimage(canvas)
        susie.createimage(canvas)
        jevil.createimage(canvas)
        ralsei.createimage(canvas)
    tikscore+=5
    win.after(5, game)
bindbutton=Bindbutton()
kris=Kris(-10,140)
jevil=Jevil(485,255)
susie=Susie(-5,200)
ralsei=Ralsei(0,260)
game()
#=========================================Настройка управления========================================
win.bind('<Key-Left>', bindbutton.left)
win.bind('<Key-Right>', bindbutton.right)
win.bind('<Key-Up>', bindbutton.up)
win.bind('<Key-Down>', bindbutton.down)
win.bind('<KeyRelease>', bindbutton.stop)
win.bind('<Key>', bindbutton.choisebutton)
win.mainloop()
