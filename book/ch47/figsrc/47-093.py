import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ds = [1, 2, 3, 4, 6, 12]
text(ax, 44, 69, r'diviseurs de 12 : 1, 2, 3, 4, 6, 12', 'fixe', 's')
text(ax, 44, 58, 'horloge à 12 heures', 'sujet', 'm')
text(ax, 44, 29, 'un autre groupe de 12 éléments', 'autre', 'm')
for i, d in enumerate(ds):
    x = 3 + i * 14.2
    box(ax, x, 40, 12.5, 11, 'resultat', label=str(d), size='m')
    bad = d == 6
    box(ax, x, 11, 12.5, 11, 'limite' if bad else 'resultat', fill=True, label=str(d), size='m', dash=bad)
text(ax, 44, 5.5, 'taille 6 : aucun sous-groupe', 'limite', 's')
text(ax, 44, 35.5, 'un sous-groupe de chaque taille', 'resultat', 's')
save(fig, '47-093')
