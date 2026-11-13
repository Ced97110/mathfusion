import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 14, 66, 60, 9, 'fixe', label='Théorème de Lagrange')
arrow(ax, (44, 66), (44, 54), 'varie')
text(ax, 62, 60, 'appliqué à', 'varie', 's')
box(ax, 14, 28, 60, 26, 'sujet', fill=True)
text(ax, 44, 49, r'$U(10)$ : 4 éléments', 'sujet', 'm')
for i, v in enumerate(['1', '3', '7', '9']):
    disc(ax, 23.5 + i * 13.7, 39, 4.5, 'sujet', label=v, size='m')
text(ax, 44, 31.5, 'la taille d’un sous-groupe divise 4', 'sujet', 's')
for x, s in [(24, 'Euler'), (64, 'Fermat')]:
    arrow(ax, (x, 28), (x, 14), 'resultat')
    box(ax, x - 18, 4, 36, 10, 'resultat', label=s)
save(fig, '47-182')
