import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, u = 28, 33, 11
for i in range(-2, 3):
    for j in range(-2, 3):
        disc(ax, cx + i*u, cy + j*u, 0.7, 'fixe')
ax.add_patch(Circle((cx, cy), u, fill=False, ec=COL['fixe'], lw=0.6, ls='--', zorder=1))
P = lambda a, b: (cx + a*u, cy + b*u)
arrow(ax, P(0, 0), P(1, 0), 'sujet')
arrow(ax, P(0, 0), P(0, 1), 'resultat')
arrow(ax, P(0, 0), P(0.71, 0.71), 'limite')
disc(ax, *P(0, 1), 1.3, 'resultat')
disc(ax, *P(0.71, 0.71), 1.3, 'limite', fill=False)
disc(ax, *P(0, 0), 0.9, 'encre')
text(ax, 58, 54, 'quart de tour :', 'resultat', 's', ha='left')
text(ax, 58, 50.5, 'sur la grille', 'resultat', 's', ha='left')
text(ax, 58, 38, 'tour de 45° :', 'limite', 's', ha='left')
text(ax, 58, 34.5, 'hors de la grille', 'limite', 's', ha='left')
text(ax, 58, 20, 'point de départ', 'sujet', 's', ha='left')
text(ax, 58, 16.5, r'$(1\ ;\ 0)$', 'sujet', 's', ha='left')
text(ax, 44, 5, 'grille L des glissements', 'fixe', 's')
save(fig, '74-081')
