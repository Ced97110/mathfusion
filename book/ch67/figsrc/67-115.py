import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
u = 18; x0 = 8
parts = [(1, r'$x$', 'sujet'), (1, r'$x+1$', 'sujet'), (2, r'$x^2+x+1$', 'sujet')]
x = x0
for d, s, r in parts:
    box(ax, x + 0.6, 50, d * u - 1.2, 12, r, label=s, size='s')
    text(ax, x + d * u / 2, 44, f'degré {d}', r, 's')
    x += d * u
brace(ax, x0, x0 + 4 * u, 64, 'sujet', label=r'$x^4-x$ : produit, degré 4', down=False)
box(ax, x0 + 0.6, 14, 3 * u - 1.2, 12, 'limite', label=r'$x^3+x+1$', size='s')
text(ax, x0 + 1.5 * u, 8, 'degré 3 : pas facteur', 'limite', 's')
text(ax, x0 + 3 * u + 9, 20, '×', 'limite', 'l')
text(ax, 44, 33, r'3 ne divise pas 2', 'limite', 's')
save(fig, '67-115')
