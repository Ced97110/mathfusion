import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 64, 14, 20, 32, 'varie', label='reçu 001')
for y, w, role, n, cap in [(40, '000', 'resultat', 1, 'une erreur'), (20, '111', 'fixe', 2, 'deux erreurs')]:
    box(ax, 4, y - 4.5, 16, 9, role, label=w)
    line(ax, [(20, y), (64, y)], 'fixe')
    for k in range(n):
        disc(ax, 36 + 12 * k, y, 2.8, 'varie')
    text(ax, 42, y - 7, cap, 'varie', 's')
text(ax, 12, 31, 'choisi', 'resultat', 's')
text(ax, 44, 5, 'choisir le moins d’erreurs', 'resultat', 's')
save(fig, '68-098')
