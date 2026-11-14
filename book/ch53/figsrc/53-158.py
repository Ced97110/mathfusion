import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
Y = 30
box(ax, 8, 70, 22, 9, 'sujet', label='message 8')
box(ax, 58, 70, 22, 9, 'autre', label='message 9')
arrow(ax, (30.5, 74.5), (57.5, 74.5), 'varie')
text(ax, 44, 79.5, '+ 1', 'varie', 's')
f = numberline(ax, 6, 80, Y, 495, 770, step=55, arrow_right=False, every=2)
text(ax, 6, Y - 9, 'multiples de 55 : un tour chacun', 'fixe', 's', ha='left')
for v, lab, side in ((512, r'$8^{3} = 512$', 'sujet'), (729, r'$9^{3} = 729$', 'autre')):
    disc(ax, f(v), Y, 1.3, side)
    text(ax, f(v), Y + 16, lab, side, 's')
# restes : de la graduation précédente jusqu'au cube
for lo, v, side in ((495, 512, 'sujet'), (715, 729, 'autre')):
    brace(ax, f(lo), f(v), Y + 3, side, label=f'reste {v - lo}', down=False)
arrow(ax, (f(512), Y + 24), (f(729), Y + 24), 'varie')
text(ax, (f(512) + f(729)) / 2, Y + 28, '+ 217 : presque 4 tours', 'varie', 's')
text(ax, 44, 8, 'aucun rapport simple avec 8 et 9', 'fixe', 's')
save(fig, '53-158')
