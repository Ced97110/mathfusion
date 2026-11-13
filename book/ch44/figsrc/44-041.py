import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 3, 62, 38, 11, 'autre', label=r'$(\gamma \circ \beta) \circ \alpha$'); box(ax, 47, 62, 38, 11, 'sujet', label=r'$\gamma \circ (\beta \circ \alpha)$')
text(ax, 44, 48, r'lire : $\alpha$, puis $\beta$, puis $\gamma$', 'varie', 'm', weight='bold')
arrow(ax, (22, 61), (34, 52), 'fixe'); arrow(ax, (66, 61), (54, 52), 'fixe')
arrow(ax, (44, 44.5), (44, 30), 'varie')
X = [12, 36, 52, 78]; Rr = [4.5, 2.5, 2.5, 4.5]
disc(ax, X[0], 28, 4.5, 'sujet', label='$x$'); disc(ax, X[1], 28, 2.5, 'fixe'); disc(ax, X[2], 28, 2.5, 'fixe'); disc(ax, X[3], 28, 4.5, 'resultat')
for i, g in enumerate([r'$\alpha$', r'$\beta$', r'$\gamma$']):
    arrow(ax, (X[i] + Rr[i] + 0.5, 28), (X[i + 1] - Rr[i + 1] - 0.5, 28), 'varie'); text(ax, (X[i] + X[i + 1]) / 2 + (-2 if i == 1 else 0), 22.5, g, 'varie', 'm')
brace(ax, X[0] - 4, X[3] + 4, 18, 'resultat', 'même départ, même arrivée', down=True)
save(fig, '44-041')
