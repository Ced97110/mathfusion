import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 88, r'$f=x^3-2x^2+4$ : valeurs de $f$', 'sujet', 's')
cands = [1, -1, 2, -2, 4, -4]
xs = [9 + i * 14 for i in range(6)]
for x, c in zip(xs, cands):
    v = c ** 3 - 2 * c ** 2 + 4
    assert v != 0
    text(ax, x, 78, f'en {c}'.replace('-', '−'), 'varie', 's')
    box(ax, x - 6, 64, 12, 9, 'fixe', label=str(v).replace('-', '−'), size='s')
text(ax, 44, 57, 'aucune valeur nulle : pas de racine', 'fixe', 's')
arrow(ax, (44, 54), (44, 47), 'resultat')
box(ax, 8, 35, 72, 11, 'resultat', label='irréductible (degré 3)', size='m')
arrow(ax, (44, 34), (44, 24), 'varie')
text(ax, 47, 29, 'outil du chapitre 61', 'varie', 's', ha='left')
box(ax, 8, 6, 72, 18, 'varie')
text(ax, 44, 18, 'question de géométrie :', 'varie', 's')
text(ax, 44, 11, 'construire à la règle et au compas', 'varie', 's')
save(fig, '54-279')
