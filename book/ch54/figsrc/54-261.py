import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 25, 64, r'dans $\mathbb{Z}$ : coefficients', 'varie', 's')
text(ax, 68, 64, r'dans $\mathbb{Z}/2$ : 0 ou 1', 'resultat', 's')
# grille de coefficients du terme en x (ligne) et de la constante (colonne), d'après deux coefficients libres
for i in range(-3, 4):
    for j in range(-3, 4):
        disc(ax, 25 + i * 5.2, 36 + j * 5.2, 1.0, 'varie')
for dx, dy in ((-20, 0), (20, 0), (0, -20), (0, 20)):
    arrow(ax, (25 + dx * 0.85, 36 + dy * 0.85), (25 + dx * 1.0, 36 + dy * 1.0), 'varie', lw=1.0)
for a in (0, 1):
    for c in (0, 1):
        disc(ax, 62 + a * 12, 31 + c * 12, 2.2, 'resultat')
box(ax, 54, 23, 28, 28, 'resultat', fill=False, dash=True)
text(ax, 25, 8, 'une infinité de cas', 'varie', 's')
text(ax, 68, 8, '4 cas : on les liste', 'resultat', 's')
save(fig, '54-261')
