import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ys = [56, 44, 32]
for y in ys:
    text(ax, 6, y, r'$\mathbb{Z}$', 'sujet', 'l')
    arrow(ax, (12, y), (58, y), 'sujet', lw=0.9, both=True)
    for x in range(16, 56, 5):
        ax.plot([x, x], [y - 1.2, y + 1.2], color=COL['sujet'], lw=0.8, zorder=1.5)
text(ax, 6, 50, r'$\oplus$', 'fixe'); text(ax, 6, 38, r'$\oplus$', 'fixe')
for y, ye in zip(ys, (47, 44, 41)):
    line(ax, [(60, y), (65, ye)], 'resultat')
box(ax, 66, 39, 20, 10, 'resultat', label='rang = 3')
box(ax, 3, 6, 40, 9, 'fixe', label='facteurs invariants : 0', size='s')
box(ax, 45, 6, 40, 9, 'fixe', label='diviseur élémentaire : aucun', size='s')
text(ax, 32, 22, 'trois copies de ℤ', 'sujet', 's')
save(fig, '60-246')
