import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 2.4; x0, y0 = 4, 8
box(ax, x0, y0, 10 * u, 10 * u, 'sujet', label=r'$x^2$', r=0.3)
box(ax, x0 + 10 * u, y0, 5 * u, 10 * u, 'varie', label=r'5$x$', r=0.3)
box(ax, x0, y0 + 10 * u, 10 * u, 4 * u, 'varie', label=r'4$x$', r=0.3)
box(ax, x0 + 10 * u, y0 + 10 * u, 5 * u, 4 * u, 'autre', label='20', r=0.3)
text(ax, 44, 51, r'$(x+4)(x+5)$ = $x^2+(p+q)x+pq$', 'encre', 's', weight='bold')
text(ax, 66, 40, r'1. lire $p$ = 4 et $q$ = 5', 'encre', 's')
text(ax, 66, 32, r'2. $p+q$ = 9, donc 9$x$', 'varie', 's')
text(ax, 66, 24, r'3. $p\times q$ = 20', 'autre', 's')
text(ax, 66, 16, r'4. $x^2$ + 9$x$ + 20', 'resultat', 's', weight='bold')
text(ax, 66, 8, r'$x$ = 1 : 30 = 5 × 6', 'resultat', 's')
save(fig, '18-063')
