import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 14, 82, 60, 11, 'sujet', label=r'Départ : 3 divise $|G|=6$')
arrow(ax, (44, 82), (44, 78), 'varie')
text(ax, 44, 73, r'classes : $6=1+2+3$', 'varie', 'm')
x = 14; centers = []
for n, role in ((1, 'fixe'), (2, 'varie'), (3, 'varie')):
    x0 = x
    for i in range(n):
        box(ax, x, 56, 9, 9, role); x += 9
    brace(ax, x0, x, 56, role, label={1: 'centre : 1', 2: 'classe : 2', 3: 'classe : 3'}[n])
    centers.append((x0 + x) / 2); x += 3
arrow(ax, (centers[1], 49), (centers[1], 42), 'varie')
box(ax, 14, 32, 60, 10, 'resultat', label=r'$C(r)$ a $6/2=3$ éléments')
arrow(ax, (44, 32), (44, 28), 'resultat')
box(ax, 14, 18, 60, 10, 'resultat', label=r'3 divise 3 : Cauchy sur $C(r)$')
arrow(ax, (44, 18), (44, 14), 'resultat')
box(ax, 14, 4, 60, 10, 'resultat', label=r"élément d'ordre 3 dans $G$")
save(fig, '50-130')
