import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, s = 6, 58, 11
P = lambda x, y: (ox + x * s, oy + y * s)
poly(ax, [P(0, 0), P(1, 0), P(3, 1), P(2, 1)], 'resultat')
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'sujet')
arrow(ax, P(1, 1.3), P(3, 1.3), 'varie', lw=1.2)
text(ax, *P(2, 1.75), 'glisse de 2', 'varie', 's')
text(ax, *P(0.5, 0.5), 'carré', 'sujet', 's')
text(ax, *P(1.9, 0.5), 'image', 'resultat', 's')
text(ax, 68, 66, 'une transvection', 'encre', 's'); text(ax, 68, 60, r'$\det=1\times1-2\times0=1$', 'encre', 's')
# product of transvections
for cx, lab in [(14, r'$\tau_1$ : det 1'), (42, r'$\tau_2$ : det 1'), (76, r'$\tau_k$ : det 1')]:
    box(ax, cx - 10, 34, 20, 10, 'sujet', label=lab, size='s')
text(ax, 28, 39, '×', 'encre', 'l'); text(ax, 59, 39, '× … ×', 'encre', 'm')
arrow(ax, (44, 33.5), (44, 28), 'encre')
box(ax, 4, 14, 80, 13, 'resultat', label=r'produit : $1\times1\times\cdots\times1=1$', size='s')
text(ax, 44, 8, 'toute transformation symplectique :', 'resultat', 's'); text(ax, 44, 3, 'déterminant 1', 'resultat', 's', weight='bold')
save(fig, '75-084')
