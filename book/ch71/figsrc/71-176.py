import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 1.5
text(ax, 22, 54, r'$(\det P)^2 \times \det A$', 'sujet', 's')
text(ax, 66, 54, r'$\det\ \mathrm{diag}(16,\ 4)$', 'autre', 's')
poly(ax, [(14, 12), (14 + 4 * k, 12), (14 + 4 * k, 12 + 16 * k), (14, 12 + 16 * k)], 'resultat')
poly(ax, [(52, 12), (52 + 16 * k, 12), (52 + 16 * k, 12 + 4 * k), (52, 12 + 4 * k)], 'resultat')
text(ax, 14 + 2 * k, 8, '4', 'varie', 's'); text(ax, 14 + 4 * k + 3, 12 + 8 * k, '16', 'sujet', 's')
text(ax, 52 + 8 * k, 8, '16', 'sujet', 's'); text(ax, 52 + 16 * k + 3, 12 + 2 * k, '4', 'autre', 's')
text(ax, 22, 44, r'$4 \times 16 = 64$', 'resultat', 's')
text(ax, 66, 44, r'$16 \times 4 = 64$', 'resultat', 's')
text(ax, 44, 30, '=', 'resultat', 'xl')
save(fig, '71-176')
