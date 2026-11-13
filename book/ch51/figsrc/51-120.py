import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 4, 44, 38, 10, 'resultat', label='intègre : oui', size='m')
box(ax, 46, 44, 38, 10, 'limite', label='corps : non', size='m')
y = 22
f = numberline(ax, 10, 66, y, 0, 4, 1)
for v in (1, 2):
    arrow(ax, (f(v), y + 1.5), (f(2 * v), y + 1.5), 'varie', curve=-0.45); text(ax, (f(v) + f(2 * v)) / 2, y + 9, r'$\times 2$', 'varie', 's')
disc(ax, f(0.5), y, 1.3, 'limite'); text(ax, f(0.5), y - 3.4, '½', 'limite', 's')
disc(ax, f(1), y, 1.3, 'resultat')
text(ax, 44, 8, '½ n’est pas un entier', 'limite', 's')
save(fig, '51-120')
