import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 25, 78, r'carré de $\eta$ = 1 ?', 'varie', 'm', weight='bold')
text(ax, 69, 78, 'chaîne de sous-groupes', 'sujet', 'm', weight='bold')
rows = [(r'$\sigma_2^2 = \sigma_4 \neq 1$', 'limite'), (r'$\sigma_3^2 = \sigma_4 \neq 1$', 'limite'), (r'$\sigma_4^2 = 1$', 'resultat')]
for (s, r), y in zip(rows, [62, 46, 30]):
    box(ax, 4, y - 6, 42, 12, r, label=s)
# chaîne G, H, {1}
box(ax, 54, 56, 30, 12, 'sujet', label=r'$G$ : 4 éléments')
box(ax, 54, 32, 30, 12, 'resultat', label=r'$H = \{1, \sigma_4\}$')
box(ax, 54, 8, 30, 12, 'fixe', label=r'$\{1\}$')
text(ax, 69, 50, r'$\supseteq$', 'fixe', 'l')
text(ax, 69, 26, r'$\supseteq$', 'fixe', 'l')
arrow(ax, (47, 30), (53, 38), 'resultat')
text(ax, 25, 14, r'seul $\sigma_4$ convient', 'resultat', 'm')
save(fig, '63-165')
