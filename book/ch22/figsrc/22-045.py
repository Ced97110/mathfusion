import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(66)
text(ax, 24, 58, r'$\sqrt{-16}$', 'limite', 'l'); text(ax, 24, 50, 'pas de valeur réelle', 'limite', 's')
text(ax, 64, 58, r'$\sqrt{16}=4$', 'resultat', 'l'); text(ax, 64, 50, 'a un sens', 'resultat', 's')
y = 24
f = numberline(ax, 8, 74, y, -16, 16, 4, labels=False)
line(ax, [(f(-16), y), (f(0), y)], 'limite', lw=2.4); line(ax, [(f(0), y), (f(16), y)], 'resultat', lw=2.4)
disc(ax, f(-16), y, 2, 'limite'); disc(ax, f(16), y, 2, 'resultat')
text(ax, f(-16), y - 5, r'$-16$', 'limite', 'm'); text(ax, f(0), y - 5, '0', 'fixe', 'm'); text(ax, f(16), y - 5, '16', 'resultat', 'm')
text(ax, 44, 8, 'radicande', 'fixe', 's')
save(fig, '22-045')
