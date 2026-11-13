import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# Haut : unités de Z sur une droite graduée
text(ax, 44, 76, 'Dans ℤ : les unités', 'sujet', 'l')
f = numberline(ax, 12, 76, 62, -3, 3, arrow_right=False)
for v in range(-3, 4):
    if v in (-1, 1):
        disc(ax, f(v), 62, 2.6, 'sujet')
    elif v != 0:
        disc(ax, f(v), 62, 1.2, 'fixe')
text(ax, 44, 50, 'seuls 1 et −1 ont un inverse entier', 'sujet', 's')
# Bas : unités de F[x] (F = rationnels)
text(ax, 44, 38, 'Dans F[x] (F = fractions) :', 'autre', 'l')
box(ax, 4, 17, 38, 14, 'resultat', label='3 × 1/3 = 1')
text(ax, 23, 12, 'constante non nulle : unité', 'resultat', 's')
box(ax, 48, 17, 36, 14, 'limite', label='x × v : degré ≥ 1')
text(ax, 66, 12, 'x : pas d’inverse', 'limite', 's')
save(fig, '56-031')
