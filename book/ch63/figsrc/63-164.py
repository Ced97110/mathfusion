import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 21, 74, 'groupe de Klein', 'autre', 'm', weight='bold')
text(ax, 67, 74, r'groupe des racines $5^{\mathrm{e}}$', 'sujet', 'm', weight='bold')
line(ax, [(44, 8), (44, 70)], 'fixe', dash=True)
text(ax, 21, 66, 'carré de chaque élément', 'fixe', 's')
text(ax, 67, 66, 'carré de chaque élément', 'fixe', 's')
ys = [54, 40, 26]
kl = [r'$\sigma$', r'$\tau$', r'$\sigma\tau$']
for e, y in zip(kl, ys):
    box(ax, 3, y - 5, 14, 10, 'autre', label=e)
    arrow(ax, (18, y), (26, y), 'varie')
    box(ax, 27, y - 5, 14, 10, 'resultat', label='1')
sq = [(r'$\sigma_2$', r'$\sigma_4$', 'sujet'), (r'$\sigma_3$', r'$\sigma_4$', 'sujet'), (r'$\sigma_4$', '1', 'resultat')]
for (e, r, rr), y in zip(sq, ys):
    box(ax, 47, y - 5, 14, 10, 'sujet', label=e)
    arrow(ax, (62, y), (70, y), 'varie')
    box(ax, 71, y - 5, 14, 10, rr, label=r)
text(ax, 21, 12, 'aucun élément d\'ordre 4', 'autre', 's')
text(ax, 67, 12, r'$\sigma_2^2 = \sigma_4 \neq 1$ : ordre 4', 'sujet', 's')
save(fig, '63-164')
