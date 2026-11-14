import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
xl_, xr_, yt, yb, h = 22, 66, 54, 14, 10
box(ax, xl_ - 10, yt, 20, h, 'sujet', label=r'$z$', size='l')
box(ax, xr_ - 10, yt, 20, h, 'varie', label=r'$z^2$', size='l')
box(ax, xl_ - 10, yb, 20, h, 'autre', label=r'$z^3$', size='l')
box(ax, xr_ - 13, yb, 26, h, 'resultat', label=r'$z^6=z$', size='l')
# chemin du haut puis du bas
arrow(ax, (xl_ + 11, yt + h / 2), (xr_ - 11, yt + h / 2), 'varie')
arrow(ax, (xl_, yt - 0.5), (xl_, yb + h + 0.5), 'autre')
arrow(ax, (xr_, yt - 0.5), (xr_, yb + h + 0.5), 'autre')
arrow(ax, (xl_ + 11, yb + h / 2), (xr_ - 14, yb + h / 2), 'varie')
text(ax, 44, yt + h + 4, r'$\eta$ : $z\mapsto z^2$', 'varie', 'm')
text(ax, xl_ + 3, 42, r'$\zeta$ : $z\mapsto z^3$', 'autre', 's', ha='left')
text(ax, xr_ - 3, 42, r'$\zeta$ : $z\mapsto z^3$', 'autre', 's', ha='right')
text(ax, 44, yb - 4, r'$\eta$ : $z\mapsto z^2$', 'varie', 'm')
text(ax, 44, 31, 'même arrivée', 'resultat', 's')
text(ax, 66, 4, r'car $z^5=1$', 'resultat', 's')
save(fig, '64-150')
