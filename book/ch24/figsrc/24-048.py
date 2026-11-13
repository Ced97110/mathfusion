import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [(40, 'sujet', 'lundi', r'$x+y$', '5'), (24, 'autre', 'mardi', r'$2x+y$', '8'), (4, 'resultat', 'somme', r'$3x+2y$', '13')]
for y, r, nom, g, d in rows:
    text(ax, 9, y + 5, nom, r, 's')
    box(ax, 18, y, 34, 10, r, fill=True, label=g)
    text(ax, 57, y + 5, '=', 'fixe', 'l')
    box(ax, 62, y, 22, 10, r, fill=True, label=d)
for xc in (35, 73):
    text(ax, xc, 37, '+', 'varie', 'l', weight='bold')
line(ax, [(18, 19), (84, 19)], 'fixe')
save(fig, '24-048')
