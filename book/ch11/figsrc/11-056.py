import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(80)
box(ax, 4, 70, 38, 6, 'resultat', label='unité d’arrivée : en haut', size='s')
box(ax, 46, 70, 38, 6, 'sujet', label='unité de départ : en bas', size='s')
def row(y, start, top, bot, end, n):
    text(ax, 12, y, start, 'sujet', 'm')
    text(ax, 28, y, r'$\times$', 'encre', 'm')
    frac(ax, 45, y, top, bot, 'resultat', 'sujet', w=13)
    text(ax, 62, y, '=', 'encre', 'm')
    text(ax, 74, y, end, 'resultat', 'm', weight='bold')
row(52, '120 min', '1 h', '60 min', '2 h', 1)
row(24, '2 h', '60 min', '1 h', '120 min', 2)
save(fig, '11-056')
