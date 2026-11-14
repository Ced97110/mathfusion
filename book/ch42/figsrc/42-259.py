import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ys = [60, 46, 32]
text(ax, 16, 70, 'départ', 'sujet', 's'); text(ax, 62, 70, 'arrivée', 'resultat', 's')
for y in ys: disc(ax, 16, y, 3.5, 'sujet'); disc(ax, 62, y, 3.5, 'resultat')
for a, b in ((0, 1), (1, 2), (2, 0)): arrow(ax, (19.7, ys[a]), (58.3, ys[b]), 'varie')
text(ax, 39, 66, r'$T_A$', 'varie')
box(ax, 2, 18, 41, 8, 'resultat', label='au moins une : surjective', size='s')
box(ax, 46, 18, 40, 8, 'resultat', label='au plus une : injective', size='s')
arrow(ax, (22, 18), (34, 10), 'resultat'); arrow(ax, (66, 18), (54, 10), 'resultat')
box(ax, 14, 2, 60, 8, 'sujet', label='bijection : un inverse existe', size='s')
save(fig, '42-259')
