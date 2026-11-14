import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# haut : 12 = 4 × 3 se coupe
box(ax, 3, 44, 18, 11, 'fixe', label='ℤ/12')
arrow(ax, (22, 49.5), (34, 49.5), 'resultat')
text(ax, 28, 54, '12 = 4 × 3', 'resultat', 's')
box(ax, 36, 44, 22, 11, 'sujet', label='ℤ/4')
box(ax, 62, 44, 22, 11, 'autre', label='ℤ/3')
text(ax, 44, 38, 'premiers entre eux : on coupe', 'resultat', 's')
line(ax, [(4, 33), (84, 33)], 'fixe', lw=0.5, dash=True)
# bas : 4 = 2 × 2 ne se coupe plus
box(ax, 3, 12, 22, 11, 'sujet', label='ℤ/4')
text(ax, 14, 27, r'ann = $(2^2)$', 'sujet', 's')
arrow(ax, (27, 17.5), (40, 17.5), 'limite')
text(ax, 33.5, 20.5, '4 = 2 × 2', 'limite', 's')
box(ax, 42, 12, 18, 11, 'fixe', label='ℤ/2', dash=True)
box(ax, 64, 12, 18, 11, 'fixe', label='ℤ/2', dash=True)
text(ax, 44, 5, '2 et 2 : facteur commun, pas de coupe', 'limite', 's')
save(fig, '60-052')
