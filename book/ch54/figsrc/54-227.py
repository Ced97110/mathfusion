import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# ligne A : f -> f barre
box(ax, 2, 78, 36, 14, 'sujet', label=r'$f=x^3+x^2+2$', size='m')
box(ax, 50, 78, 36, 14, 'autre', label=r'$\bar{f}$ dans $\mathbb{Z}/3$', size='m')
arrow(ax, (38.5, 85), (49.5, 85), 'varie')
text(ax, 44, 89.5, 'modulo 3', 'varie', 's')
# ligne B : trois valeurs
text(ax, 44, 71, r'valeurs de $\bar{f}$ : aucune nulle', 'autre', 's')
for i, v in enumerate([2, 1, 2]):
    box(ax, 4 + i * 28.5, 56, 25.5, 10, 'autre', label=rf'$\bar{{f}}({i})={v}$', size='m')
text(ax, 44, 49, 'degré 3 sans racine : irréductible', 'autre', 's')
# ligne C : f barre irréductible
arrow(ax, (20, 46), (20, 36), 'autre')
box(ax, 2, 22, 36, 14, 'autre', label=r'$\bar{f}$ irréductible', size='m')
# retour : une factorisation de f donnerait une de f barre
text(ax, 62, 42, r'si $f=gh$ alors $\bar f=\bar g\bar h$', 'varie', 's')
arrow(ax, (38.5, 29), (49.5, 29), 'resultat')
box(ax, 50, 22, 36, 14, 'resultat', label=r'$f$ irréductible sur $\mathbb{Q}$', size='s')
text(ax, 44, 12, r'$\bar f$ irréductible $\Rightarrow$ $f$ irréductible', 'resultat', 's', weight='bold')
save(fig, '54-227')
