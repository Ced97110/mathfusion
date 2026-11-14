import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
bw, bh = 26, 11
xl, xr = 4, 58
yt, yb = 56, 12
box(ax, xl, yt, bw, bh, 'sujet', label=r'$\sigma_2$')
box(ax, xr, yt, bw, bh, 'sujet', label=r'$\sigma_2^2 = \sigma_4$')
box(ax, xr, yb, bw, bh, 'sujet', label=r'$\sigma_2^3 = \sigma_3$')
box(ax, xl, yb, bw, bh, 'resultat', label=r'$\sigma_2^4 = 1$')
cl, cr = xl + bw / 2, xr + bw / 2
arrow(ax, (xl + bw + 0.5, yt + bh / 2), (xr - 0.5, yt + bh / 2), 'varie')
arrow(ax, (cr, yt - 0.5), (cr, yb + bh + 0.5), 'varie')
arrow(ax, (xr - 0.5, yb + bh / 2), (xl + bw + 0.5, yb + bh / 2), 'varie')
arrow(ax, (cl, yb + bh + 0.5), (cl, yt - 0.5), 'varie')
text(ax, 44, yt + bh / 2 + 3.5, r'$2 \times 2 = 4$', 'varie', 's')
text(ax, cr - 2.5, 48, r'$4 \times 2 = 8$, reste 3', 'varie', 's', ha='right')
text(ax, 44, yb + bh / 2 - 3.5, r'$3 \times 2 = 6$, reste 1', 'varie', 's')
text(ax, cl + 2.5, 32, r'$1 \times 2 = 2$', 'varie', 's', ha='left')
text(ax, 44, 40, r'$G \cong \mathbb{Z}/4\mathbb{Z}$', 'resultat', 'l')
text(ax, 44, 4, '4 puissances distinctes : tout le groupe', 'fixe', 's')
save(fig, '63-162')
