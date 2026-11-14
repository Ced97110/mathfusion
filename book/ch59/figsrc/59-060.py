import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 3.3
pts = sorted({(4 * a + 6 * b, 6 * a + 4 * b) for a in range(-6, 7) for b in range(-6, 7) if -1 <= 4 * a + 6 * b <= 11 and -3 <= 6 * a + 4 * b <= 13})
def panel(x0, title, third, label3):
    P = lambda a, b: (x0 + (a + 1) * u, 10 + (b + 3) * u)
    box(ax, x0 - 1, 8, 12 * u + 2, 16 * u + 2, 'fixe', fill=False, dash=True, lw=0.6)
    for p in pts:
        disc(ax, *P(*p), 0.9, 'sujet')
    arrow(ax, P(0, 0), P(4, 6), 'fixe', lw=1.5)
    arrow(ax, P(0, 0), P(*third), 'varie', lw=1.5)
    text(ax, P(4, 6)[0] - 4.5, P(4, 6)[1] + 1.5, r'$f_1$', 'fixe', 'm')
    if third == (6, 4):
        text(ax, P(6, 4)[0] + 3.5, P(6, 4)[1] - 3.5, label3, 'varie', 'm')
    else:
        text(ax, P(10, 10)[0] - 6, P(10, 10)[1] + 0.5, label3, 'varie', 'm')
    text(ax, x0 + 6 * u, 10 + 16 * u + 5, title, 'encre', 'm')
panel(3, 'avant', (6, 4), r'$f_2$')
panel(46, 'après', (10, 10), r'$f_2+f_1$')
text(ax, 44, 3.5, r'les mêmes points de $K$', 'sujet', 'm')
save(fig, '59-060')
