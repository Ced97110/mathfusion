import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 2, 55, "ensembles seulement (ch. 43)", 'fixe', 's', ha='left')
text(ax, 2, 31, "avec l'opération (ch. 48)", 'sujet', 's', ha='left')
xs = [3, 33, 63]
for x, l in zip(xs, ["entiers", "4 paquets", "4 positions"]): box(ax, x, 38, 22, 11, 'fixe', label=l, size='s')
for x, l in zip(xs, [r"entiers, $+$", r"4 paquets, $+$", r"4 positions, $+$"]): box(ax, x, 14, 22, 11, 'sujet', label=l, size='s')
for a in (25, 55):
    arrow(ax, (a, 43.5), (a + 8, 43.5), 'fixe'); arrow(ax, (a, 19.5), (a + 8, 19.5), 'varie')
text(ax, 44, 5, "chaque flèche respecte la somme", 'varie', 's')
save(fig, '48-076')
