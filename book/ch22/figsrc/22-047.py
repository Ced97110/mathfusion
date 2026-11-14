import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(56)
y = 22
f = numberline(ax, 8, 72, y, 1, 8, 1)
text(ax, 44, 50, r'$x\geq3$', 'resultat', 'l')
line(ax, [(f(3), y), (f(8), y)], 'resultat', lw=2.4)
disc(ax, f(2), y, 1.8, 'limite'); disc(ax, f(3), y, 1.8, 'resultat'); disc(ax, f(7), y, 1.8, 'resultat')
text(ax, f(2), y + 16, r'radicande $-1$', 'limite', 's'); arrow(ax, (f(2), y + 13.5), (f(2), y + 3), 'limite')
text(ax, f(3), y + 9, r'$\sqrt{0}=0$', 'resultat', 's'); arrow(ax, (f(3), y + 7.2), (f(3), y + 3), 'resultat')
text(ax, f(7), y + 9, r'$\sqrt{4}=2$', 'resultat', 's'); arrow(ax, (f(7), y + 7.2), (f(7), y + 3), 'resultat')
save(fig, '22-047')
