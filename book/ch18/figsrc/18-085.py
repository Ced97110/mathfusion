import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, u = 12, 10, 6
X, T, D = 4 * u, 3 * u, 2 * u
box(ax, x0, y0 + D, X, X, 'sujet', label=r'$x^2$', r=0.4)
box(ax, x0 + X, y0 + D, T, X, 'varie', label=r'$3x$', r=0.4)
box(ax, x0, y0, X, D, 'varie', label=r'$2x$', r=0.4)
box(ax, x0 + X, y0, T, D, 'fixe', label='6', r=0.4)
brace(ax, x0, x0 + X + T, y0 + D + X + 1, 'sujet', label=r'$x+3$', down=False)
text(ax, x0 - 4, y0 + D / 2 + X / 2 + D / 2, r'$x+2$', 'sujet', rot=90)
text(ax, 58, 52, r'$x=1$ : $3\times4=12$', 'resultat', 's', ha='left')
text(ax, 58, 44, r'$x=4$ : $6\times7=42$', 'resultat', 's', ha='left')
text(ax, 58, 30, r'$2+3=5$', 'varie', 's', ha='left')
text(ax, 58, 22, r'$2\times3=6$', 'fixe', 's', ha='left')
save(fig, '18-085')
