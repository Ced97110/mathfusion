import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(56)
y = 30
text(ax, 8, y, '36', 'sujet', 'l'); text(ax, 15, y, 'po', 'sujet', 'l')
text(ax, 25, y, r'$\times$', 'encre', 'l')
text(ax, 42, y + 4, '1 pied', 'resultat', 'l')
text(ax, 39, y - 4, '12', 'sujet', 'l'); text(ax, 46, y - 4, 'po', 'sujet', 'l')
line(ax, [(32, y), (53, y)], 'encre', lw=0.9)
text(ax, 62, y, '=', 'encre', 'l')
text(ax, 71, y, '3', 'resultat', 'l'); text(ax, 80, y, 'pied', 'resultat', 'l')
for (sx, sy) in ((15, y), (46, y - 4)):
    line(ax, [(sx - 3.2, sy - 3), (sx + 3.2, sy + 3)], 'varie', lw=1.4)
text(ax, 30, 12, 'les deux « po » se barrent', 'varie', 's')
text(ax, 72, 44, 'il reste le pied', 'resultat', 's')
save(fig, '11-057')
