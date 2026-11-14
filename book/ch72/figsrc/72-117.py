import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def trip(y, vals, role):
    for i, v in enumerate(vals):
        box(ax, 6 + i * 14, y, 12, 9, role, label=v)
def pair(yb, a, b):
    yt = yb + 24
    trip(yt, a, 'sujet'); trip(yb, b, 'resultat')
    for i, j in ((0, 2), (2, 0)):
        arrow(ax, (12 + i * 14, yt), (12 + j * 14, yb + 9), 'varie')
    arrow(ax, (26, yt), (26, yb + 9), 'fixe')
    text(ax, 66, yb + 16, r'$S_d$', 'varie', 'l', weight='bold')
pair(46, ['1', '0', '0'], ['0', '0', '1'])
pair(8, ['4', '5', '6'], ['6', '5', '4'])
save(fig, '72-117')
