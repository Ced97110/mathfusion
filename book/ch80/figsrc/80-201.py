import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$\mathbb{Z}/2=\{0,\ 1\}$', 'sujet', 'l')
text(ax, 14, 45, 'élément', 'fixe', 's'); text(ax, 52, 45, 'au carré', 'fixe', 's')
for k, v in enumerate((0, 1)):
    y = 34 - k * 18
    box(ax, 6, y - 6, 16, 12, 'sujet', label=str(v), size='l')
    arrow(ax, (22, y), (36, y), 'varie')
    box(ax, 36, y - 6, 32, 12, 'resultat', label=rf'${v}\times{v}={v}$', size='m')
    text(ax, 78, y, 'vrai', 'resultat', 's')
text(ax, 44, 4, 'deux tests : la règle tient', 'resultat', 'm')
save(fig, '80-201')
