import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = [15, 44, 73]; lab = ['1', '4', '1']; rl = ['sujet', 'fixe', 'resultat']
for x, l, r in zip(X, lab, rl): disc(ax, x, 48, 5, r, label=l, size='l')
arrow(ax, (20.5, 48), (38.5, 48), 'varie'); arrow(ax, (49.5, 48), (67.5, 48), 'autre')
text(ax, 29.5, 53, r'$\alpha$', 'varie', 'l'); text(ax, 58.5, 53, r'$\beta$', 'autre', 'l')
arrow(ax, (15, 42.5), (73, 42.5), 'sujet', curve=0.3)
text(ax, 44, 27, r'$\beta \circ \alpha$', 'sujet', 'l')
text(ax, 44, 12, r'le résultat reste dans $S$', 'sujet', 'm')
save(fig, '44-035')
