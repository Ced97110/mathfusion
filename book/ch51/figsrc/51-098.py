import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, r = 24, 38, 17
P = {k: (cx + r * math.sin(math.radians(90 * k)), cy + r * math.cos(math.radians(90 * k))) for k in range(4)}
for k in range(4):
    disc(ax, *P[k], 4, 'sujet' if k == 2 else 'fixe', label=str(k), size='m')
# 0 -> 2 puis 2 -> 0 : deux fois 2 heures
arrow(ax, (P[0][0] + 1.5, P[0][1] - 4.2), (P[2][0] + 1.5, P[2][1] + 4.2), 'varie')
arrow(ax, (P[2][0] - 1.5, P[2][1] + 4.2), (P[0][0] - 1.5, P[0][1] - 4.2), 'varie')
text(ax, cx + 6.5, cy, '2 h', 'varie', 's'); text(ax, cx - 6.5, cy, '2 h', 'varie', 's')
text(ax, cx, 8, 'Cadran à 4 heures', 'fixe', 's')
box(ax, 50, 40, 34, 22, 'limite', fill=True)
text(ax, 67, 56, r'dans $\mathbb{Z}/4$', 'limite', 's')
text(ax, 67, 49, r'$2 \times 2 = 0$', 'limite', 'l')
text(ax, 67, 43.5, r'$2 \neq 0$', 'sujet', 's')
box(ax, 50, 8, 34, 22, 'resultat')
text(ax, 67, 24, r'dans $\mathbb{Z}$', 'resultat', 's')
text(ax, 67, 17, r'$2 \times 3 = 6$', 'resultat', 'm')
text(ax, 67, 11.5, 'aucun produit nul', 'resultat', 's')
save(fig, '51-098')
