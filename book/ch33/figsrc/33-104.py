import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1, y0, A = 10, 76, 12, 30
X = lambda d: x0 + d / 180 * (x1 - x0)
Y = lambda v: y0 + v * A
numberline(ax, x0, x1, y0, 0, 180, step=30, labels=False, arrow_right=False)
line(ax, [(X(d), Y(math.sin(math.radians(d)))) for d in range(0, 181, 3)], 'sujet', lw=1.6)
for d, s, r in ((0, '0', 'fixe'), (30, r'$\pi/6$', 'resultat'), (90, r'$\pi/2$', 'fixe'), (150, r'$5\pi/6$', 'sujet'), (180, r'$\pi$', 'fixe')):
    text(ax, X(d), y0 - 3.8, s, r, 's', weight='bold' if r != 'fixe' else 'normal')
text(ax, 4.5, Y(0.5), '1/2', 'fixe', 's')
arrow(ax, (X(150) - 2, Y(0.5)), (X(30) + 2.5, Y(0.5)), 'varie')
text(ax, X(90), Y(0.5) - 5, 'arcsin', 'varie', 's')
for d, r in ((30, 'resultat'), (150, 'sujet')):
    line(ax, [(X(d), y0), (X(d), Y(0.5))], r, lw=0.7, dash=True)
    disc(ax, X(d), Y(0.5), 1.6, r)
text(ax, X(90), Y(1) + 4, r'$\sin x$', 'sujet', 's')
save(fig, '33-104')
