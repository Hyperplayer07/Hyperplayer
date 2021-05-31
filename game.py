from ursina import *  # 창 프로그램 플러그인 포함 
from random import *

from ursina.mesh_importer import ursina_mesh_to_obj  # 랜덤 프로그램 플러그인 포함

app = Ursina()

window.borderless = False  #창이 움직일 수 있도록 만듬
window.color = color._20   #창 색깔 

ua = 1   #ua,ub,uc,ud,ue 변수의 값을 1로 설정
ub = 1
uc = 1
ud = 1
ue = 1

mone = 0  #mone을 0값으로 설정
mone_text = Text(text=str(mone), x=-0.62, y=0.3, scale=2, background=True) #mone의 값을 지정된 좌표에 보이기
bone = Button(text='red +1', color=color.red, x=-0.6, scale=0.19)  #bone이라는 버튼을 생성, 지정된좌표에 빨간색으로 보이기

def bone_click():    #bone 버튼을 클릭한다면 ua만큼 mone값을 올리기
    global mone
    mone += ua       

bone.on_click = bone_click

mtwo = 0  #mtwo의 값을 0으로 설정
ranptwo = 0  #ranptwo의 값을 0으로 설정
mtwo_text = Text(text=str(mtwo), x=-0.33, y=0.3, scale=2, background=True) #mtwo의 값을 지정된 좌표에 보이기
ranptwo_text = Text(text=str(ranptwo), x=-0.31, y=0.37, scale=1.2, background=True) #ranptwo의 값을 지정된 좌표에 보이기
Text(text='+', x=-0.33, y= 0.37, scale=1, background=True)  #'+'를 지정된 좌표에 보이기
btwo = Button(text='9 red = orange', color=color.orange, x=-0.3, scale=0.19)  #btwo이라는 버튼을 생성, 지정된좌표에 주황색으로 보이기

def btwo_click():    #btwo 버튼을 클릭한다면 ub만큼 mtwo값을 올리기
    global mtwo
    global mone
    if mone >= 9 :
        mone -= 9
        mtwo += ub
        rantwo = (randrange(1, 6))
        if rantwo >= 5 :             #20%확률로 mtwo값이 1증가한다(+값)
            global ranptwo
            mtwo += 1
            ranptwo += 1
        
btwo.on_click = btwo_click   

mthr = 0   #mthr을 0값으로 설정
ranpthr = 0
mthr_text = Text(text=str(mthr), x=-0.02, y=0.3, scale=2, background=True)
ranpthr_text = Text(text=str(ranpthr), x=0, y=0.37, scale=1.2, background=True)
Text(text='+', x=-0.02, y= 0.37, scale=1, background=True)
bthr = Button(text='8 orange = green', color=color.green, x=0, scale=0.19)

def bthr_click():    
    global mthr
    global mtwo
    if mtwo >= 8 :
        mtwo -= 8
        mthr += uc
        ranthr = (randrange(1, 6))
        if ranthr >= 5 :            
            global ranpthr
            mthr += 1
            ranpthr += 1

bthr.on_click = bthr_click   

mfour = 0   
ranpfour = 0
mfour_text = Text(text=str(mfour), x=0.25, y=0.3, scale=2, background=True)
ranpfour_text = Text(text=str(ranpfour), x=0.27, y=0.37, scale=1.2, background=True)
Text(text='+', x=0.25, y= 0.37, scale=1, background=True)
bfour = Button(text='7 green = blue', color=color.blue, x=0.27, scale=0.19)

def bfour_click():    
    global mfour
    global mthr
    if mthr >= 7 :
        mthr -= 7
        mfour += ud
        ranfour = (randrange(1, 6))
        if ranfour >= 5 :            
            global ranpfour
            mfour += 1
            ranpfour += 1

bfour.on_click = bfour_click 

mfive = 0   
ranpfive = 0
mfive_text = Text(text=str(mfive), x=0.55, y=0.3, scale=2, background=True)
ranpfive_text = Text(text=str(ranpfive), x=0.57, y=0.37, scale=1.2, background=True)
Text(text='+', x=0.55, y= 0.37, scale=1, background=True)
bfive = Button(text='10 blue = pink', color=color.pink, x=0.57, scale=0.19)

def bfive_click():    
    global mfive
    global mfour
    if mfour >= 10 :
        mfour -= 10
        mfive += ue
        ranfive = (randrange(1, 6))
        if ranfive >= 5 :            
            global ranpfive
            mfive += 1
            ranpfive += 1

bfive.on_click = bfive_click

Text(text=('UPGRADE'), x=-0.657, y=-0.11)
upone = Button(text='red upgade = 1 green', color=color.red, x=-0.6, y=-0.17, scale=0.059)
uptwo = Button(text='orange upgade = 1 blue', color=color.orange, x=-0.6, y=-0.24, scale=0.059)
upthr = Button(text='green upgade = 1 pink', color=color.green, x=-0.6, y=-0.31, scale=0.059)
upfour = Button(text='blue upgade = 5 pink', color=color.blue, x=-0.6, y=-0.38, scale=0.059)
upfive = Button(text='pink upgade = 20 pink', color=color.pink, x=-0.6, y=-0.45, scale=0.059)

def upone_click():    
    global ua
    global mthr
    if mthr >= 1 :
        ua += 1
        mthr -= 1 

def uptwo_click():
    global ub
    global mfour 
    if mfour >= 1 :
        ub += 1
        mfour -= 1

def upthr_click():
    global uc
    global mfive
    if mfive >= 1 :
        uc += 1
        mfive -= 1

def upfour_click():
    global ud
    global mfive
    if mfive >= 5 :
        ud += 1
        mfive -= 5

def upfive_click():
    global ue
    global mfive
    if mfive >= 20 :
        ue += 1
        mfive -= 20

upone.on_click = upone_click
uptwo.on_click = uptwo_click
upthr.on_click = upthr_click
upfour.on_click = upfour_click
upfive.on_click = upfive_click

Text(text=('GAMBLING on 10'), x=-0.4, y=-0.11)
doone = Button(text='red', color=color.red, x=-0.3, y=-0.17, scale=0.059)
dotwo = Button(text='orange', color=color.orange, x=-0.3, y=-0.24, scale=0.059)
dothr = Button(text='green', color=color.green, x=-0.3, y=-0.31, scale=0.059)
dofour = Button(text='blue', color=color.blue, x=-0.3, y=-0.38, scale=0.059)
dofive = Button(text='pink', color=color.pink, x=-0.3, y=-0.45, scale=0.059)

def doone_click():
    global mone
    if mone >= 10 :
        doa = (randrange(1, 3))
        if doa == 1 :
            mone += 10
            doa -= 1
        if doa == 2 :
            mone -= 10
            doa -= 2

def dotwo_click():
    global mtwo
    if mtwo >= 10 :
        dob = (randrange(1, 3))
        if dob == 1 :
            mtwo += 10
            dob -= 1
        if dob == 2 :
            mtwo -= 10
            dob -= 2

def dothr_click():
    global mthr
    if mthr >= 10 :
        doc = (randrange(1, 3))
        if doc == 1 :
            mthr += 10
            doc -= 1
        if doc == 2 :
            mthr -= 10
            doc -= 2

def dofour_click():
    global mfour
    if mfour >= 10 :
        dod = (randrange(1, 3))
        if dod == 1 :
            mfour += 10
            dod -= 1
        if dod == 2 :
            mfour -= 10
            dod -= 2

def dofive_click():
    global mfive
    if mfive >= 10 :
        doe = (randrange(1, 3))
        if doe == 1 :
            mfive += 10
            doe -= 1
        if doe == 2 :
            mfive -= 10
            doe -= 2

doone.on_click = doone_click
dotwo.on_click = dotwo_click
dothr.on_click = dothr_click
dofour.on_click = dofive_click
dofive.on_click = dofour_click

def update():                      
    global mone
    mone_text.text = str(mone)
    global mtwo
    mtwo_text.text = str(mtwo)
    global ranptwo
    ranptwo_text.text = str(ranptwo)
    global mthr
    mthr_text.text = str(mthr)
    global ranpthr
    ranpthr_text.text = str(ranpthr)
    global mfour
    mfour_text.text = str(mfour)
    global ranpfour
    ranpfour_text.text = str(ranpfour)
    global mfive
    mfive_text.text = str(mfive)
    global ranpfive
    ranpfive_text.text = str(ranpfive)

app.run()