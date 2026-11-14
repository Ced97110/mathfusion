import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 7.0; x0, y0 = 4, 8
box(ax, x0, y0, 2 * u, 2 * u, 'sujet', label='4', r=0.3)
box(ax, x0 + 2 * u, y0, 3 * u, 2 * u, 'varie', label='6', r=0.3)
box(ax, x0, y0 + 2 * u, 2 * u, 3 * u, 'varie', label='6', r=0.3)
box(ax, x0 + 2 * u, y0 + 2 * u, 3 * u, 3 * u, 'autre', label='9', r=0.3)
text(ax, 44, 59, r'$x^2+6x+9=(x+3)^2$', 'encre', 'l', weight='bold')
text(ax, 66, 46, r'1er : $x^2$, carré de $x$', 'sujet', 's')
text(ax, 66, 39, '3 au bout : 9 = 3²', 'autre', 's')
text(ax, 66, 32, r'milieu : 6$x$ = 2 × $x$ × 3', 'varie', 's')
text(ax, 66, 21, r'$x$ = 2 : 4 + 12 + 9 = 25', 'resultat', 's', weight='bold')
text(ax, 66, 14, r'$(2+3)^2$ = 5² = 25', 'resultat', 's', weight='bold')
save(fig, '18-061')
