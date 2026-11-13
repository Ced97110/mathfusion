import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

# grille de 16 carreaux, côté inconnu
for i in range(4):
    for j in range(4):
        box(ax, 8 + 4*i, 40 + 4*j, 4, 4, 'sujet', lw=0.6, r=0)
text(ax, 16, 61, '16 carreaux', 'sujet', 's')
text(ax, 16, 36, '?', 'varie', 'm', weight='bold')
text(ax, 5, 48, '?', 'varie', 'm', weight='bold')

# sens habituel et sens renversé
text(ax, 58, 56, 'avant : côté connu → aire', 'fixe', 's')
text(ax, 58, 47, 'ici : aire 16 → côté ?', 'varie', 's')

# droite graduée 0 à 25 : abscisse = 6 + 3,12 × valeur
f = numberline(ax, 6, 84, 20, 0, 25, step=1, labels=False, arrow_right=False)
for v, lab in ((0, '0'), (9, '9'), (16, '16'), (25, '25')):
    text(ax, f(v), 15.5, lab, 'fixe', 's')
text(ax, 44, 8, 'nombre de carreaux', 'fixe', 's')

# valeur visée 16
line(ax, [(f(16), 18), (f(16), 22)], 'sujet', lw=1.4)

# essais 1 (3), 2 (5), 3 (4)
disc(ax, f(9), 20, 1.2, 'limite')
text(ax, f(9), 27, '1) 3 × 3 = 9, trop petit', 'limite', 's')
disc(ax, f(25), 20, 1.2, 'limite')
text(ax, 86, 27, '2) 5 × 5 = 25, trop grand', 'limite', 's', ha='right')
ax.add_patch(Circle((f(16), 20), 1.2, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=6))
text(ax, f(16), 33, '3) 4 × 4 = 16, juste', 'resultat', 's')

save(fig, '04-005')
