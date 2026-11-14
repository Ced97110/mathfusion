import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'dans $2\mathbb{Z}$ : pas de $1$, pas d\'inverse'.replace("\\'", "'"), 'fixe', 's')
x0, x1 = 14, 74
fx = lambda v: x0 + (v + 4) / 8 * (x1 - x0)
line(ax, [(fx(-4) - 3, 62), (fx(4) + 3, 62)], 'fixe')
for v in range(-4, 5):
    if v % 2 == 0:
        disc(ax, fx(v), 62, 1.6, 'fixe')
disc(ax, fx(1), 62, 1.6, 'limite', fill=False)
text(ax, fx(1), 55, '1 absent', 'limite', 's')
text(ax, 44, 44, r'dans $S=\mathbb{Z}\times2\mathbb{Z}$', 'sujet', 's')
box(ax, 4, 6, 80, 32, 'sujet')
text(ax, 44, 32, r'$(1,-2)\times(1,-2)$', 'autre', 'm')
text(ax, 44, 24, r'$1\times1=1$', 'sujet', 's')
text(ax, 44, 17, r'$-2-2+4=0$', 'sujet', 's')
text(ax, 44, 10, '(1, 0) : le neutre', 'resultat', 's')
save(fig, '56-195')
