import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(66)
text(ax, 18, 58, 'forme générale', 'fixe', 's'); text(ax, 68, 58, 'exemple', 'fixe', 's')
def stack(x, a, u, b, v, size):
    text(ax, x - 4, 40, a, 'resultat', size, weight='bold'); text(ax, x + 5, 40, u, 'resultat', size, weight='bold')
    text(ax, x - 4, 25, b, 'sujet', size, weight='bold'); text(ax, x + 5, 25, v, 'sujet', size, weight='bold')
    line(ax, [(x - 11, 32.5), (x + 11, 32.5)], 'encre', lw=0.9)
stack(18, '$a$', '$u$', '$b$', '$v$', 'xl')
stack(68, '1', 'pied', '12', 'po', 'xl')
arrow(ax, (31, 40), (51, 40), 'fixe', lw=0.8)
arrow(ax, (31, 25), (51, 25), 'fixe', lw=0.8)
text(ax, 18, 11, 'haut : unité voulue', 'resultat', 's'); text(ax, 68, 11, 'bas : unité quittée', 'sujet', 's')
save(fig, '11-058')
