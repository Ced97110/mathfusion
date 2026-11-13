import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
bx, bw, bh = 8, 72, 11
ys = [90, 73, 56, 39]
box(ax, bx, ys[0], bw, bh, 'sujet', label=r'ordres = puissances de $p$', size='m')
box(ax, bx, ys[1], bw, bh, 'autre', label=r'un premier $r\neq p$ divise $|G|$', size='m')
box(ax, bx, ys[2], bw, bh, 'varie', label=r"Cauchy : élément d'ordre $r$", size='m', lw=1.8)
box(ax, bx, ys[3], bw, bh, 'limite', label='contradiction', size='m')
for k in range(3):
    arrow(ax, (44, ys[k]), (44, ys[k + 1] + bh + 0.5), 'encre')
line(ax, [(2, 34), (86, 34)], 'fixe', dash=True)
text(ax, 3, 29, r'$\mathbb{Z}/6\mathbb{Z}$ : 3 divise 6', 'encre', 's', ha='left')
xs = [14 + 11 * i for i in range(6)]
for i in range(6):
    disc(ax, xs[i], 17, 3.8, 'varie' if i in (0, 2, 4) else 'fixe', label=str(i), size='m')
arrow(ax, (xs[0] + 1, 21.5), (xs[2] - 1, 21.5), 'varie', curve=-0.5)
arrow(ax, (xs[2] + 1, 21.5), (xs[4] - 1, 21.5), 'varie', curve=-0.5)
arrow(ax, (xs[4] - 1, 12.5), (xs[0] + 1, 12.5), 'varie', curve=-0.2)
text(ax, 66, 5, "élément 2 : ordre 3", 'limite', 's')
save(fig, '50-031')
