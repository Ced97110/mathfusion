import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(58)
y = 22
f = numberline(ax, 8, 72, y, -5, -2, 0.5)
text(ax, 44, 52, r'$m\geq-\frac{7}{2}$', 'resultat', 'l')
line(ax, [(f(-3.5), y), (f(-2), y)], 'resultat', lw=2.4)
disc(ax, f(-4), y, 1.8, 'limite'); disc(ax, f(-3.5), y, 1.8, 'sujet'); disc(ax, f(-3), y, 1.8, 'resultat')
text(ax, f(-4) - 2, y + 9, r'radicande $-1$', 'limite', 's'); arrow(ax, (f(-4), y + 7.2), (f(-4), y + 3), 'limite')
text(ax, f(-3) + 2, y + 9, 'radicande 1', 'resultat', 's'); arrow(ax, (f(-3), y + 7.2), (f(-3), y + 3), 'resultat')
text(ax, f(-3.5), y + 17, r'limite $-3{,}5$', 'sujet', 's'); arrow(ax, (f(-3.5), y + 15), (f(-3.5), y + 3), 'sujet')
save(fig, '22-048')
