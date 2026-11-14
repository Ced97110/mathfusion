import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
Ox, Oy, u = 22, 36, 14
Px = Ox + u
line(ax, [(Px, Oy - 22), (Px, Oy + 22)], 'fixe', lw=1.3)
text(ax, Px + 1.5, Oy + 25, 'courbe en $P$', 'fixe', 's', ha='left')
arrow(ax, (Ox, Oy), (Px - 0.3, Oy), 'sujet', lw=1.6)
text(ax, (Ox + Px) / 2, Oy - 4, r'$(1,\ 0)$', 'sujet', 's')
arrow(ax, (Px, Oy + 9), (Px - 2 * u, Oy + 9), 'autre', lw=1.6)
text(ax, Px - u, Oy + 12.5, r'$(-2,\ 0)$', 'autre', 's')
disc(ax, Ox, Oy, 1.0, 'fixe')
text(ax, Ox - 3, Oy + 2.5, r'$O$', 'fixe', 's')
disc(ax, Px, Oy, 1.3, 'resultat')
text(ax, Px + 3, Oy - 3.5, r'$P$', 'resultat', 's')
for y0 in (Oy, Oy + 9):
    line(ax, [(Px - 2, y0), (Px - 2, y0 + 2), (Px, y0 + 2)], 'fixe', lw=0.6)
text(ax, 44, 68, 'les deux sont perpendiculaires\nà la courbe', 'encre', 's')
box(ax, 60, 22, 26, 26, 'resultat', label='parallèles :\n$1\\times0$\n$-\\,0\\times(-2)$\n$=0$, donc $q=0$', size='s')
save(fig, '70-144')
