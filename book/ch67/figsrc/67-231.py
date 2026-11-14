import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 4, 56, 28, 10, 'sujet', label=r'$f=x^2+1$')
arrow(ax, (33, 61), (47, 61), 'varie')
box(ax, 48, 56, 36, 10, 'sujet', label=r'discriminant $=-4$')
text(ax, 44, 49, r"calcul : résultant de $f$ et $f'$", 'varie', 's')
for x, v, ro in [(8, '2', 'limite'), (24, '3', 'resultat'), (40, '5', 'resultat'), (56, '7', 'resultat')]:
    box(ax, x, 24, 12, 9, ro, label=v)
text(ax, 76, 28.5, '…', 'fixe', 'm')
text(ax, 14, 38, r'2 divise $-4$', 'limite', 's')
brace(ax, 24, 68, 23, 'resultat', label="Dedekind s'applique")
save(fig, '67-231')
