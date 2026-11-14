import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
B, K = 12, 6.5
ax.add_patch(Rectangle((4, B), 80, 2 * K, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=1))
text(ax, 44, B + K + 0.5, 'horloge : hauteurs 0, 1, 2', 'resultat', 's')
for x, h in ((20, 0), (44, 0), (68, 6)):
    line(ax, [(x, B), (x, B + K * h)], 'fixe', dash=True)
    disc(ax, x, B + K * h, 1.6, 'varie')
    text(ax, x, 6, f'$x={ {20: 0, 44: 1, 68: 2}[x] }$', 'fixe', 's')
text(ax, 20, B - 3.5 + 7.5, '0', 'varie', 's')
text(ax, 44, B - 3.5 + 7.5, '0', 'varie', 's')
text(ax, 60, B + K * 6 + 8, '6 : hors de l’horloge', 'varie', 's')
save(fig, '55-012')
