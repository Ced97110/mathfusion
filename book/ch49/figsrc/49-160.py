import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 2, 96, 'départ : deux gestes, même point', 'fixe', 's', ha='left')
cx, cy, h = 20, 80, 8
P = {'A': (cx-h, cy-h), 'B': (cx+h, cy-h), 'C': (cx+h, cy+h), 'D': (cx-h, cy+h)}
poly(ax, list(P.values()), 'fixe')
for k, (x, y) in P.items():
    disc(ax, x, y, 2.6, 'resultat' if k == 'B' else 'fixe', label=k, size='s')
disc(ax, 56, 87, 3.8, 'sujet', label=r'$r$', size='s'); disc(ax, 56, 73, 3.8, 'sujet', label=r'$rs$', size='s')
arrow(ax, (52.5, 86), (30.5, 73.5), 'varie'); arrow(ax, (52.5, 74), (31, 72.3), 'varie')
text(ax, 74, 80, 'même point', 'resultat', 's')
text(ax, 2, 62, "l'étape qui porte le poids", 'fixe', 's', ha='left')
box(ax, 6, 44, 76, 12, 'varie')
text(ax, 44, 50, r'$r^{-1}(rs) = s \in \mathrm{Stab}\,A$', 'varie', 'm')
text(ax, 2, 36, 'arrivée : même classe latérale', 'fixe', 's', ha='left')
box(ax, 20, 10, 48, 20, 'varie', fill=True)
disc(ax, 34, 20, 4, 'sujet', label=r'$r$', size='s'); disc(ax, 54, 20, 4, 'sujet', label=r'$rs$', size='s')
save(fig, '49-160')
