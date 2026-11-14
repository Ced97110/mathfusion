import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 15, 82, r'$U(8)$', 'sujet', 'm', weight='bold'); text(ax, 73, 82, r'$U(12)$', 'autre', 'm', weight='bold')
for i, (a, b) in enumerate([(1, 1), (3, 5), (5, 7), (7, 11)]):
    y = 70 - i * 10
    box(ax, 8, y - 4, 14, 8, 'fixe' if i == 0 else 'sujet', label=str(a), size='m')
    box(ax, 66, y - 4, 14, 8, 'fixe' if i == 0 else 'autre', label=str(b), size='m')
    arrow(ax, (23, y), (65, y), 'varie')
text(ax, 44, 74, 'bijection', 'varie', 's')
text(ax, 15, 28, r'$3\times5=7$', 'sujet', 'm'); text(ax, 73, 28, r'$5\times7=11$', 'autre', 'm')
arrow(ax, (28, 28), (58, 28), 'resultat')
text(ax, 44, 32, 'même forme', 'resultat', 's')
box(ax, 6, 6, 76, 12, 'resultat', label='le produit est conservé', size='m')
save(fig, '45-235')
