import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 18, 66, 'étage de tour', 'sujet', 'm', weight='bold')
text(ax, 70, 66, 'groupe de Galois', 'autre', 'm', weight='bold')
rows = [(50, 'racine carrée', '2 éléments : abélien', 'lemmes 1, 2', True),
        (31, 'racine cubique', '3 éléments : abélien', 'lemmes 1, 2', True),
        (12, r'racine $p$-ième', r"cyclique d'ordre $p$", 'lemme 3', False)]
for y, a, b, lab, fwd in rows:
    box(ax, 2, y, 32, 10, 'sujet', label=a, size='s')
    box(ax, 54, y, 32, 10, 'autre', label=b, size='s')
    if fwd:
        arrow(ax, (35, y + 5), (53, y + 5), 'varie')
        text(ax, 44, y + 9, lab, 'varie', 's')
    else:
        arrow(ax, (53, y + 5), (35, y + 5), 'resultat')
        text(ax, 44, y + 9, lab, 'resultat', 's')
save(fig, '64-144')
