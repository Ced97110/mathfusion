import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def panel(cx, kind):
    x0, y0, w = cx - 11, 26, 22
    box(ax, x0 - 1, y0 - 1, w + 2, w + 2, 'fixe', fill=False, lw=0.5)
    if kind == 0:
        line(ax, [(x0 + 1, y0 + 5), (x0 + w - 1, y0 + 15)], 'sujet', lw=1.3)
        line(ax, [(x0 + 1, y0 + 11), (x0 + w - 1, y0 + 21)], 'autre', lw=1.3)
    elif kind == 1:
        line(ax, [(x0 + 1, y0 + 4), (x0 + w - 1, y0 + 19)], 'sujet', lw=1.3)
        line(ax, [(x0 + 1, y0 + 19), (x0 + w - 1, y0 + 6)], 'autre', lw=1.3)
        disc(ax, x0 + 10.6, y0 + 11.7, 1.2, 'resultat')
    else:
        line(ax, [(x0 + 1, y0 + 5), (x0 + w - 1, y0 + 18)], 'sujet', lw=2.2)
        line(ax, [(x0 + 1, y0 + 5), (x0 + w - 1, y0 + 18)], 'autre', lw=0.9, dash=True)
panel(15, 0); panel(44, 1); panel(73, 2)
text(ax, 15, 21, '0 point', 'encre', 's')
text(ax, 44, 21, '1 point', 'resultat', 's')
text(ax, 73, 21, 'une infinité', 'encre', 's')
text(ax, 15, 56, 'parallèles', 'fixe', 's')
text(ax, 44, 56, 'sécantes', 'fixe', 's')
text(ax, 73, 56, 'confondues', 'fixe', 's')
box(ax, 22, 4, 44, 9, 'limite', label=r'jamais $2$ points', size='m')
save(fig, '24-087')
