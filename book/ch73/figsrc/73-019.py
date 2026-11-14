import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 17; oy = 14
def cells(x0, n, role):
    for i in range(n): box(ax, x0 + i * u, oy, u, u, role, r=0.2)
cells(4, 1, 'fixe'); cells(40, 2, 'varie')
text(ax, 4 + u / 2, oy + u / 2, 'aire 1', 'fixe', 's')
text(ax, 40 + u, oy + u / 2, 'aire 2', 'varie', 'm')
brace(ax, 4, 4 + u, oy, 'fixe', 'largeur 1')
brace(ax, 40, 40 + 2 * u, oy, 'varie', 'largeur 2')
text(ax, 2.5, oy + u + 3, 'hauteur 1', 'fixe', 's', ha='left')
line(ax, [(40 + 2 * u + 2.5, oy), (40 + 2 * u + 2.5, oy + u)], 'fixe', lw=0.8)
text(ax, 40 + 2 * u + 4, oy + u / 2, '1', 'fixe', 's', ha='left')
arrow(ax, (4 + u + 2, oy + u / 2), (38, oy + u / 2), 'varie')
text(ax, 29.5, oy + u / 2 + 3.5, '×2', 'varie', 's')
text(ax, 44, 46, r'$(x,\,y)\mapsto(2x,\,y)$', 'varie', 'l')
text(ax, 44, 5, r'$\det=2$ : aire $2\times1$', 'varie', 's')
save(fig, '73-019')
