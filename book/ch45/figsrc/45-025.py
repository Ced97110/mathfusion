import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'dans la définition', 'encre', 's')
for i, (g, n, s, role) in enumerate(((r'$G$ : horloge', 'neutre 0', r'$1$', 'sujet'), (r"$G'$ : rotations", r'neutre $r_0$', r"$1'$", 'autre'))):
    y = 34 - 20 * i
    text(ax, 14, y + 8, g, role, 's')
    box(ax, 4, y - 6, 22, 11, role, label=n, size='s')
    arrow(ax, (27, y - 0.5), (52, y - 0.5), 'varie')
    box(ax, 53, y - 7, 18, 13, 'resultat', label=s, size='xl')
text(ax, 77, 28, 'même\nsigne', 'fixe', 's') if False else None
text(ax, 44, 3, "le trait ' désigne l'autre groupe", 'fixe', 's')
save(fig, '45-025')
