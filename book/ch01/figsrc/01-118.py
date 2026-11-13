import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [30 + 8 * i for i in range(7)]
R = 1.6
def row(y):
    line(ax, [(27, y - R), (82, y - R)], 'fixe', lw=0.5)
row(58); row(42); row(26)
for x in xs:
    for y in (58, 42, 26): disc(ax, x, y, R, 'fixe', fill=False)
for i, x in enumerate(xs): text(ax, x, 12, str(i), 'fixe', 's')
# rangée 1
text(ax, 3, 58, 'départ', 'encre', 's', ha='left')
disc(ax, xs[0], 58, R, 'resultat')
# rangée 2
text(ax, 3, 42, '4 et 5 vérifiés', 'encre', 's', ha='left')
disc(ax, xs[4], 42, R, 'resultat'); disc(ax, xs[5], 42, R, 'resultat')
ax.add_patch(Circle((xs[6], 42), R, ec=COL['limite'], fc='white', ls='--', lw=0.9, zorder=3))
text(ax, 72, 36.5, 'rien pour 6', 'limite', 's')
# rangée 3
text(ax, 3, 26, 'passage', 'sujet', 'm', ha='left', weight='bold')
for x in xs[:-1]: arrow(ax, (x + 1.6, 27.5), (x + 6.4, 27.5), 'varie', curve=-0.6)
text(ax, 54, 19.5, r'si vrai en $n$, vrai en $n + 1$', 'varie', 's')
save(fig, '01-118')
