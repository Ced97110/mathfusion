import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(70)
y = 30
f = numberline(ax, 8, 74, y, -5, 5, 1, labels=False)
text(ax, 24, 62, r'$\sqrt{16}=-4$', 'limite', 'l'); text(ax, 24, 55, 'faux', 'limite', 's')
text(ax, 64, 62, r'$\sqrt{16}=4$', 'resultat', 'l'); text(ax, 64, 55, 'vrai', 'resultat', 's')
arrow(ax, (24, 52), (f(-4), y + 3.5), 'limite')
arrow(ax, (64, 52), (f(4), y + 3.5), 'resultat')
disc(ax, f(4), y, 2.2, 'resultat'); disc(ax, f(-4), y, 2.2, 'autre'); disc(ax, f(0), y, 1.2, 'fixe')
text(ax, f(4), y - 5, '4', 'resultat', 'm'); text(ax, f(-4), y - 5, r'$-4$', 'autre', 'm'); text(ax, f(0), y - 5, '0', 'fixe', 'm')
text(ax, f(4), y - 11, r'$4^2=16$', 'resultat', 's'); text(ax, f(-4), y - 11, r'$(-4)^2=16$', 'autre', 's')
save(fig, '22-036')
