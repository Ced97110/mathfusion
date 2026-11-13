import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 3, 24, 82, 44, 'sujet', fill=False, dash=True)
text(ax, 44, 63, r'groupe orthogonal : $P^TAP=A$', 'sujet', 's')
for i, lab in enumerate(['diag(1, 1)', 'diag(1, −1)', 'diag(−1, −1)']):
    box(ax, 6 + i*27.3, 36, 25, 11, 'sujet', label=lab, size='s')
text(ax, 44, 53, 'trois transformations du groupe', 'sujet', 's')
arrow(ax, (47, 35), (74, 35), 'resultat', curve=-0.35)
text(ax, 44, 27.5, 'enchaînées : elles restent dedans', 'resultat', 's')
box(ax, 3, 3, 82, 12, 'autre', fill=True, dash=True, label='voisin : groupe symplectique', size='s')
text(ax, 44, 19.5, 'même idée : conserver une forme', 'autre', 's')
save(fig, '71-216')
