import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$n_p\equiv1\ (\mathrm{mod}\ 3)$', 'encre', 'l')
y = 24
xs = {v: 9 + (v - 1) * 7.78 for v in range(1, 11)}
line(ax, [(xs[1], y), (xs[10], y)], 'fixe', lw=0.6)
for v in range(1, 11):
    disc(ax, xs[v], y, 3.1, 'resultat' if v % 3 == 1 else 'limite', label=str(v), size='m')
for a, b in [(1, 4), (4, 7), (7, 10)]:
    arrow(ax, (xs[a], y + 4.5), (xs[b], y + 4.5), 'varie', curve=-0.5)
text(ax, (xs[1] + xs[4]) / 2, y + 13, '+3', 'varie', 'm')
disc(ax, 6, 8, 2.2, 'resultat'); text(ax, 10, 8, 'reste 1 : convient', 'resultat', 's', ha='left')
disc(ax, 49, 8, 2.2, 'limite'); text(ax, 53, 8, 'autre reste : écarté', 'limite', 's', ha='left')
save(fig, '50-048')
