import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ys = [64, 40, 16]
left = [r'$G$ : 4 éléments', r'$H$ : 2 éléments', r'$\{1\}$ : 1 élément']
right = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{3})$', r'$E$']
for y, l, r in zip(ys, left, right):
    box(ax, 3, y, 28, 11, 'sujet', label=l, size='s')
    box(ax, 62, y, 22, 11, 'autre', label=r, size='s')
    line(ax, [(31, y + 5.5), (62, y + 5.5)], 'fixe', dash=True)
text(ax, 17, 57, r'$[G:H]=2$', 'resultat', 's')
text(ax, 17, 33, r'$|H|=2$', 'varie', 's')
text(ax, 73, 57, r"$[\mathrm{Inv}\,H:F]=2$", 'resultat', 's')
text(ax, 73, 33, r"$[E:\mathrm{Inv}\,H]=2$", 'varie', 's')
text(ax, 46.5, 57, '=', 'resultat', 'l', weight='bold')
text(ax, 46.5, 33, '=', 'varie', 'l', weight='bold')
text(ax, 44, 4, r'$F=\mathbb{Q}$, $H=\{1,\sigma\}$', 'fixe', 's')
save(fig, '63-127')
