from ursina import *
from random import randrange

app = Ursina()
window.borderless = False
window.color = color._20

# 자원과 업그레이드 수치
mone = mtwo = mthr = mfour = mfive = 0
ranptwo = ranpthr = ranpfour = ranpfive = 0
ua = ub = uc = ud = ue = 1  # 자동 수집 용도 (현재 전환에는 미사용)

# 시크릿 변수
creata = creatb = creatc = creatd = create = 0
ca = cb = cc = 0

# 텍스트 객체 관리용 딕셔너리
texts = {}

def make_text(name, value, x, y, scale=2):
    texts[name] = Text(text=str(value), x=x, y=y, scale=scale, background=True)

make_text("mone", mone, -0.62, 0.3)
make_text("mtwo", mtwo, -0.33, 0.3)
make_text("ranptwo", ranptwo, -0.31, 0.37, 1.2)
make_text("mthr", mthr, -0.02, 0.3)
make_text("ranpthr", ranpthr, 0, 0.37, 1.2)
make_text("mfour", mfour, 0.25, 0.3)
make_text("ranpfour", ranpfour, 0.27, 0.37, 1.2)
make_text("mfive", mfive, 0.55, 0.3)
make_text("ranpfive", ranpfive, 0.57, 0.37, 1.2)

for x, y in [(-0.33, 0.37), (-0.02, 0.37), (0.25, 0.37), (0.55, 0.37)]:
    Text(text='+', x=x, y=y, scale=1, background=True)

# 버튼 함수
bone = Button(text='red +1', color=color.red, x=-0.6, scale=0.19,
              on_click=lambda: globals().__setitem__('mone', mone + 1))

def convert_button(label, color, x, cost_var, cost_amt, gain_var, rand_var):
    def on_click():
        if globals()[cost_var] >= cost_amt:
            globals()[cost_var] -= cost_amt
            globals()[gain_var] += 1
            if randrange(1, 6) >= 5:
                globals()[gain_var] += 1
                globals()[rand_var] += 1
    return Button(text=label, color=color, x=x, scale=0.19, on_click=on_click)

btwo = convert_button('9 red = orange', color.orange, -0.3, 'mone', 9, 'mtwo', 'ranptwo')
bthr = convert_button('8 orange = green', color.green, 0, 'mtwo', 8, 'mthr', 'ranpthr')
bfour = convert_button('7 green = blue', color.blue, 0.27, 'mthr', 7, 'mfour', 'ranpfour')
bfive = convert_button('10 blue = pink', color.pink, 0.57, 'mfour', 10, 'mfive', 'ranpfive')

# 업그레이드 버튼
Text(text='UPGRADE', x=-0.657, y=-0.11)
def upgrade_button(text_prefix, color, x, y, cost_var, cost_amt, upgrade_var):
    def on_click():
        if globals()[cost_var] >= cost_amt:
            globals()[upgrade_var] += 1
            globals()[cost_var] -= cost_amt
    return Button(text='', color=color, x=x, y=y, scale=0.059, on_click=on_click)

upone = upgrade_button('red upgrade', color.red, -0.6, -0.17, 'mthr', 1, 'ua')
uptwo = upgrade_button('orange upgrade', color.orange, -0.6, -0.24, 'mfour', 1, 'ub')
upthr = upgrade_button('green upgrade', color.green, -0.6, -0.31, 'mfive', 1, 'uc')
upfour = upgrade_button('blue upgrade', color.blue, -0.6, -0.38, 'mfive', 5, 'ud')
upfive = upgrade_button('pink upgrade', color.pink, -0.6, -0.45, 'mfive', 20, 'ue')

# 도박 버튼
Text(text='GAMBLING on 10', x=-0.4, y=-0.11)
def gamble_button(label, color, x, y, var):
    def on_click():
        if globals()[var] >= 10:
            if randrange(1, 3) == 1:
                globals()[var] += 10
            else:
                globals()[var] -= 10
    return Button(text=label, color=color, x=x, y=y, scale=0.059, on_click=on_click)

doone = gamble_button('red', color.red, -0.3, -0.17, 'mone')
dotwo = gamble_button('orange', color.orange, -0.3, -0.24, 'mtwo')
dothr = gamble_button('green', color.green, -0.3, -0.31, 'mthr')
dofour = gamble_button('blue', color.blue, -0.3, -0.38, 'mfour')
dofive = gamble_button('pink', color.pink, -0.3, -0.45, 'mfive')

# 시크릿 섹션
Text(text='SECRET FOUND', x=-0.091, y=-0.11)
def secret_add_button(name, color, x, y, var, cost_var):
    def on_click():
        if globals()[cost_var] >= 1:
            globals()[cost_var] -= 1
            globals()[var] += 1
    return Button(text=f'{name} +0', color=color, x=x, y=y, scale=0.11, on_click=on_click)

creatone = secret_add_button('red', color.red, -0.02, -0.2, 'creata', 'mone')
creattwo = secret_add_button('orange', color.orange, 0.13, -0.2, 'creatb', 'mtwo')
creatthr = secret_add_button('green', color.green, 0.28, -0.2, 'creatc', 'mthr')
creatfour = secret_add_button('blue', color.blue, 0.03, -0.335, 'creatd', 'mfour')
creatfive = secret_add_button('pink', color.pink, 0.18, -0.335, 'create', 'mfive')
createqual = Button(text='=', color=color.black, x=0.375, y=-0.2725, scale=0.08)
Text(text='SECRET', x=0.475, y=-0.26)
creatreset = Button(text='reset', color=color.black50, x=0.52, y=-0.4, scale=0.11)

def creatreset_click():
    global creata, creatb, creatc, creatd, create
    creata = creatb = creatc = creatd = create = 0
creatreset.on_click = creatreset_click

def createqual_click():
    global ca, cb, cc, uc, ud, ue
    combos = [
        ((1, 3, 2, 5, 4), 'ue', 3, 'SECRET 1', 'ca'),
        ((2, 7, 9, 1, 2), 'ud', 3, 'SECRET 2', 'cb'),
        ((1, 2, 3, 2, 1), 'uc', 3, 'SECRET 3', 'cc')
    ]
    for cond, target, amt, msg, count_var in combos:
        if (creata, creatb, creatc, creatd, create) == cond:
            globals()[target] += amt
            Text(text=msg, x=-0.05, y=-0.15)
            creatreset_click()
            globals()[count_var] += 1

    if ca >= 1 and cb >= 1 and cc >= 1:
        Button(text='You win!', color=color.black, x=0, y=0.3, scale=5)
createqual.on_click = createqual_click

# 실시간 텍스트 갱신
def update():
    for key in texts:
        texts[key].text = str(globals()[key])

    creatone.text = f'red +{creata}'
    creattwo.text = f'orange +{creatb}'
    creatthr.text = f'green +{creatc}'
    creatfour.text = f'blue +{creatd}'
    creatfive.text = f'pink +{create}'

    upone.text = f'red upgrade = +{ua}'
    uptwo.text = f'orange upgrade = +{ub}'
    upthr.text = f'green upgrade = +{uc}'
    upfour.text = f'blue upgrade = +{ud}'
    upfive.text = f'pink upgrade = +{ue}'

app.run()
