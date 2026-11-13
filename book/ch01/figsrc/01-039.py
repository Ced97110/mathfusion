import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import FancyArrowPatch
fig, ax = canvas(50)
f = numberline(ax, 6, 58, 26, 0, 5, arrow_right=False)
line(ax, [(58, 26), (86, 26)], 'fixe')
text(ax, 66, 29, '…', 'fixe', 'm')
X = [f(v) for v in range(6)]
for x in X: disc(ax, x, 26, 1.3, 'sujet'); ax.patches[-1].set_zorder(3.5)
for a, b in zip(X[:-1], X[1:]): arrow(ax, (a, 27.4), (b, 27.4), 'varie', lw=0.9, curve=-0.6)
ax.add_patch(FancyArrowPatch((58, 27.4), (64, 27.4), arrowstyle='-|>', mutation_scale=7, lw=0.9, color=COL['varie'],
             connectionstyle='arc3,rad=-0.6', ls='--', zorder=4))
line(ax, [(76, 24.5), (76, 27.5)], 'limite', lw=0.9)
disc(ax, 76, 26, 1.6, 'limite'); ax.patches[-1].set_zorder(3.5)
text(ax, 76, 34, 'en trop', 'limite', 's', weight='bold')
text(ax, 76, 19, 'jamais atteint', 'limite', 's')
brace(ax, 6, 58, 20, 'resultat', label='atteints depuis 0 : ℕ')
text(ax, 66, 7, "l'axiome 3 l'interdit", 'limite', 's', weight='bold')
text(ax, 32, 44, 'Comptez : 0, 1, 2, 3 …', 'encre', 'm')
save(fig, '01-039')
