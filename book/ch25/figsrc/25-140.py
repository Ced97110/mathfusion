import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
rows = ((32, '1', '45°'), (14, '0,5', '≈ 26,565°'))
text(ax, 44, 42, 'une seule réponse par nombre', 'sujet', 's')
for y, n, a in rows:
    box(ax, 4, y - 4.5, 16, 9, 'fixe', label=n)
    box(ax, 33, y - 4.5, 22, 9, 'sujet', label='arctan', lw=1.2)
    box(ax, 66, y - 4.5, 20, 9, 'resultat', label=a)
    arrow(ax, (21, y), (32, y), 'varie'); arrow(ax, (56, y), (65, y), 'varie')
text(ax, 12, 4, 'rapport', 'fixe', 's'); text(ax, 76, 4, 'angle', 'resultat', 's')
save(fig, '25-140')
