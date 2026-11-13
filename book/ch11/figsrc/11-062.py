import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(80)
def row(y, num, den, ok):
    c = 'resultat' if ok else 'limite'
    box(ax, 2, y - 5, 22, 10, 'sujet', label='36 po', size='m')
    text(ax, 30, y, r'$\times$', 'encre', 'm')
    frac(ax, 54, y, num, den, 'fixe' if ok else 'sujet', 'sujet' if ok else 'fixe', w=20, dy=4)
    if ok:
        box(ax, 43.5, y - 8.2, 21, 6.4, c, fill=False, lw=1.0)
    else:
        box(ax, 43.5, y + 1.8, 21, 6.4, c, fill=False, lw=1.0)
    text(ax, 44, y - 16, 'po en bas : il se barre' if ok else 'po en haut : rien ne se barre', c, 's')
row(60, '1 pied', '12 po', True)
row(26, '12 po', '1 pied', False)
save(fig, '11-062')
