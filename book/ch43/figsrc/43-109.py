import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def grid(x0, y0, nr, nc, c):
    for r in range(nr):
        for k in range(nc):
            box(ax, x0 + k * c, y0 + (nr - 1 - r) * c, c, c, 'varie' if r == 0 else 'sujet', lw=0.5, r=0.2)
grid(20, 40, 2, 3, 6); grid(58, 40, 4, 5, 5)
text(ax, 29, 58, r'$|T| = 3$', 'sujet', 's'); text(ax, 70.5, 66, r'$|T| = 5$', 'sujet', 's')
text(ax, 18, 46, r'$|S| = 2$', 'sujet', 's', ha='right'); text(ax, 56, 50, r'$|S| = 4$', 'sujet', 's', ha='right')
text(ax, 29, 32, '2 × 3 = 6 couples', 'resultat', 's'); text(ax, 70.5, 32, '4 × 5 = 20 couples', 'resultat', 's')
text(ax, 44, 12, r'$|S \times T| = |S| \times |T|$', 'resultat', 'l')
save(fig, '43-109')
