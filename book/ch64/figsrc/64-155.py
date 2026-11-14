import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
bw, bh = 22, 10
xl_, xm_, xr_ = 2, 33, 64
ym, yt, yb = 31, 52, 10
box(ax, xl_, ym, bw, bh, 'sujet', label=r'$r$')
box(ax, xm_, yt, bw, bh, 'varie', label=r'$z^2r$')
box(ax, xm_, yb, bw, bh, 'autre', label=r'$z^3r$')
box(ax, xr_, ym, bw + 0, bh, 'resultat', label=r'$z^5r=r$')
# chemin du haut : sigma puis tau
arrow(ax, (xl_ + bw / 2 + 3, ym + bh + 0.3), (xm_ - 0.5, yt + 3), 'varie')
arrow(ax, (xm_ + bw + 0.5, yt + 3), (xr_ + bw / 2 - 3, ym + bh + 0.3), 'autre')
# chemin du bas : tau puis sigma
arrow(ax, (xl_ + bw / 2 + 3, ym - 0.3), (xm_ - 0.5, yb + 7), 'autre')
arrow(ax, (xm_ + bw + 0.5, yb + 7), (xr_ + bw / 2 - 3, ym - 0.3), 'varie')
text(ax, 14, 52, r'$\sigma$ : $\times z^2$', 'varie', 's')
text(ax, 74, 52, r'$\tau$ : $\times z^3$', 'autre', 's')
text(ax, 14, 10, r'$\tau$ : $\times z^3$', 'autre', 's')
text(ax, 74, 10, r'$\sigma$ : $\times z^2$', 'varie', 's')
text(ax, 44, 67, r'$z$ est dans $F$ : fixé par $\sigma$', 'resultat', 's')
text(ax, 44, 31 + 5, 'même arrivée', 'resultat', 's')
save(fig, '64-155')
