from ursina import *

app = Ursina()

window.borderless = False
window.color = color._20

Text.default_font = '/System/Library/Fonts/AppleSDGothicNeo.ttc'

gold = 0
gold_text = Text(text=str(gold), x=-0.02, y=0.3, scale=2, background=True)
button = Button(text='1G', color=color.blue, x=-0.6, scale=0.4)

def button_click():
    global gold
    gold += 1

button.on_click = button_click

def update():
    global gold

    gold_text.text = str(gold)

app.run()