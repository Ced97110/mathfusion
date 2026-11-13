import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rows = [(r'$(h_1k_1)(h_2k_2)$', 'sujet'), (r'$h_1(k_1h_2)k_2$', 'fixe'), (r'$h_1(h_2k_1)k_2$', 'fixe'), (r'$(h_1h_2)(k_1k_2)$', 'resultat')]
ys = [86, 62, 38, 14]
for (s, r), y in zip(rows, ys):
    box(ax, 10, y, 50, 11, r, label=s)
for a, b in zip(ys[:-1], ys[1:]):
    arrow(ax, (35, a), (35, b + 11), 'fixe')
text(ax, 84, 91, 'départ', 'sujet', 's'); text(ax, 84, 19, 'arrivée', 'resultat', 's')
box(ax, 62, 48, 24, 15, 'varie')
text(ax, 74, 59, 'étape clé', 'varie', 's'); text(ax, 74, 53, r'$k_1h_2=h_2k_1$', 'varie', 's')
arrow(ax, (62, 55.5), (36.5, 55.5), 'varie')
text(ax, 18, 94, 'regrouper les $h$, puis les $k$', 'fixe', 's', ha='left') if False else None
save(fig, '45-213')
