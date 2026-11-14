import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 24; y0 = 12; xs = [3, 32, 61]
mk = lambda x0: (lambda x, y: (x0 + (x + 1) * s / 5, y0 + (y + 1) * s / 5))
for k, x0 in enumerate(xs):
    m = mk(x0)
    if k == 0:
        poly(ax, [m(-1, -1), m(4, -1), m(4, 4), m(-1, 4)], 'fixe', fill=False)
        line(ax, [m(-1, 0), m(3, 4)], 'varie', lw=1.2); line(ax, [m(-1, 4), m(4, -1)], 'sujet', lw=1.2)
        c = m(1, 2); disc(ax, c[0], c[1], 1.3, 'resultat')
    elif k == 1:
        poly(ax, [m(-1, -1), m(4, -1), m(4, 4), m(-1, 4)], 'fixe', fill=False)
        poly(ax, [m(-1, -1), m(-1, 0), m(1, 2), m(4, -1)], 'resultat')
        line(ax, [m(-1, 0), m(3, 4)], 'varie', lw=1.2); line(ax, [m(-1, 4), m(4, -1)], 'sujet', lw=1.2)
    else:
        m = lambda x, y, x0=x0: (x0 + (x + 1) * s / 8, y0 + (y + 1) * s / 8)
        poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
        poly(ax, [m(0, 0), m(6, 0), m(0, 4)], 'resultat')
        c = m(0, 4); disc(ax, c[0], c[1], 1.5, 'varie')
        text(ax, *m(0.6, 4.0), r'$x+2y$', 'varie', 's', ha='left')
cap = ['équations', 'inéquations', 'optimisation']
sub = ['un point', 'une zone', 'le meilleur point']
for k, x0 in enumerate(xs):
    r = 'sujet' if k == 2 else 'fixe'
    text(ax, x0 + s / 2, y0 + s + 5, cap[k], r, 's', weight='bold' if k == 2 else 'normal')
    text(ax, x0 + s / 2, y0 - 5, sub[k], r, 's')
save(fig, '20-107')
