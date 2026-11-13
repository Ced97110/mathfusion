import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
c = 5
# left family: two flat squares a x a (a = 2), each with 4 cells
for x in (12, 26):
    box(ax, x, 24, 2 * c, 2 * c, 'sujet', r=0.3)
    line(ax, [(x + c, 24.5), (x + c, 24 + 2 * c - 0.5)], 'sujet', lw=0.4, dash=True)
    line(ax, [(x + 0.5, 24 + c), (x + 2 * c - 0.5, 24 + c)], 'sujet', lw=0.4, dash=True)
    text(ax, x + c, 24 + 2 * c + 3, r'$a^2$', 'sujet', 's')
text(ax, 8, 29, r'$-$', 'sujet', 'xl', weight='bold')
text(ax, 25, 49, r'$-2a^2$', 'sujet', 'l')
text(ax, 25, 17, 'exposant 2', 'varie', 'm', weight='bold')
# right family: one cube a x a x a
cubes(ax, [(i, j, k) for i in range(2) for j in range(2) for k in range(2)], (68, 22), c, 'autre')
text(ax, 68, 49, r'$a^3$', 'autre', 'l')
text(ax, 68, 17, 'exposant 3', 'varie', 'm', weight='bold')
text(ax, 47, 29, r'$\neq$', 'fixe', 'xl', weight='bold')
text(ax, 44, 8, 'pas de regroupement', 'limite', 'm', weight='bold')
text(ax, 44, 59, r'pour $a=2$', 'fixe', 's')
save(fig, '15-043')
