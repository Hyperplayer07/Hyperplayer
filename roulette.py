from ursina import *
from random import *

app = Ursina()

window.borderless = False  
window.color = color._20 

Text.default_font = '/System/Library/Fonts/AppleSDGothicNeo.ttc'

a = 0
b = 0
c = 0 

a_text = Text(text=str(a), x=-0.62, y=0.3, scale=2, background=True)
b_text = Text(text=str(b), x=-0.02, y=0.3, scale=2, background=True)
c_text = Text(text=str(c), x=0.58, y=0.3, scale=2, background=True)
roulette = Button(text='click!', color=color.green, scale=0.2)
def roulette_click():    
    global a
    global b
    global c
    a = (randrange(1, 35))
    b = (randrange(1, 35))
    c = (randrange(1, 35))

if a == b :
    b = (randrange(1, 35))

if b == c :
    c = (randrange(1, 35))

if c == a :
     a = (randrange(1, 35))

roulette.on_click = roulette_click

def update():                      #mone,mtwo,mthr의 값을 실시간으로 텍스트로 설정
    global a
    a_text.text = str(a)
    global b
    b_text.text = str(b)
    global c
    c_text.text = str(c)

app.run()