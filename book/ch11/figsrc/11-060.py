import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(62)
text(ax, 22, 56, 'de 36 po vers pieds', 'fixe', 's'); text(ax, 66, 56, 'de pieds vers pouces', 'fixe', 's')
for cx, top, bot, rt, rb, bn in ((22, '1 pied', '12 po', 'resultat', 'sujet', 12), (66, '12 po', '1 pied', 'resultat', 'sujet', 1)):
    frac(ax, cx, 38, top, bot, rt, rb, w=18, size='m', dy=4)
    box(ax, cx - 11, 30.2, 22, 7.2, 'sujet', fill=False, dash=True)
    text(ax, cx, 14, f'$b$ = {bn}', 'sujet', 'l', weight='bold')
    text(ax, cx, 6, 'départ en bas', 'sujet', 's')
save(fig, '11-060')
