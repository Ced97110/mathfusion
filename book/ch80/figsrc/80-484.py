import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'dans les entiers 0, 1, 2, 3', 'fixe', 'm')
text(ax, 17, 62, 'pas de résultat', 'limite', 's'); text(ax, 65, 62, 'nombre d’un autre genre', 'resultat', 's')
for y, a, b in [(42, r'$3 - 5$', 'nombres négatifs'), (24, r'$3 \div 4$', 'fractions'), (6, r'$\sqrt{2}$', 'radicaux')]:
    box(ax, 4, y, 26, 12, 'limite', label=a)
    box(ax, 44, y, 40, 12, 'resultat', label=b)
    arrow(ax, (31, y + 6), (43, y + 6), 'varie')
save(fig, '80-484')
