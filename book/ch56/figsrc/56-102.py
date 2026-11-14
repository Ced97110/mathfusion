import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx = [16, 44, 72]
for x, letter, en, fr in zip(cx, 'ACC', ['ascending', 'chain', 'condition'], ['ascendante', 'de chaîne', 'condition']):
    box(ax, x - 10, 54, 20, 14, 'sujet', label=letter, size='xl')
    arrow(ax, (x, 54), (x, 47), 'fixe')
    box(ax, x - 13, 37, 26, 10, 'fixe', label=en, size='s')
    arrow(ax, (x, 37), (x, 30), 'fixe')
    box(ax, x - 13, 20, 26, 10, 'resultat', label=fr, size='s')
text(ax, 44, 12, 'toute suite croissante', 'resultat', 's')
text(ax, 44, 7, "d'idéaux devient constante", 'resultat', 's')
save(fig, '56-102')
