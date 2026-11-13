import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
ox, oy, s = 16, 10, 11
X = lambda v: ox + s * v
Y = lambda v: oy + s * v
arrow(ax, (ox, oy), (X(5.4), oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy), (ox, Y(7.4)), 'fixe', lw=0.9)
text(ax, X(5.4) + 3, oy, r'$x$', 'fixe', 's')
text(ax, ox - 3, Y(7.4) + 1, r'$y$', 'fixe', 's')
for v in (1, 4):
    line(ax, [(X(v), oy), (X(v), Y(7))], 'fixe', lw=0.5, dash=True)
    text(ax, X(v), oy - 2.6, str(v), 'fixe', 's')
line(ax, [(X(0), Y(5)), (X(5), Y(0))], 'sujet', lw=1.2)
line(ax, [(X(0.5), Y(7)), (X(4), Y(0))], 'autre', lw=1.2)
line(ax, [(X(0), Y(6.5)), (X(13 / 3), Y(0))], 'resultat', lw=1.4, dash=True)
text(ax, X(0) - 1.5, Y(5), r'$D_1$', 'sujet', 's', ha='right')
text(ax, X(0.5), Y(7) + 3, r'$D_2$', 'autre', 's')
text(ax, X(0) - 1.5, Y(6.5), r'$D_1+D_2$', 'resultat', 's', ha='right')
f1 = lambda x: 5 - x
f2 = lambda x: 8 - 2 * x
f3 = lambda x: (13 - 3 * x) / 2
for x, dx in ((1, 2.4), (4, 2.6)):
    for f, r, lab in ((f1, 'sujet', f1(x)), (f2, 'autre', f2(x)), (f3, 'resultat', f3(x))):
        disc(ax, X(x), Y(f(x)), 0.9, r)
        yy = Y(f(x)) + (1.8 if (x == 4 and f is f2) else 0)
        text(ax, X(x) + dx, yy, f'{lab:g}'.replace('.', ','), r, 's', ha='left')
disc(ax, X(3), Y(2), 1.1, 'encre')
text(ax, X(3) + 3, Y(2) + 3, r'$P$', 'encre', 'm')
save(fig, '24-052')
