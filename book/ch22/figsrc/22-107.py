import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 6, 44, 34, 10, 'sujet', label=r'$\sqrt{y-3}$'); text(ax, 45, 49, '=', 'encre', 'l'); box(ax, 50, 44, 16, 10, 'autre', label='4')
for cx in (23, 58):
    arrow(ax, (cx, 44), (cx, 32), 'varie'); text(ax, cx + 3, 38, 'au carré', 'varie', 's', ha='left')
box(ax, 6, 22, 34, 10, 'sujet', label=r'$y-3$'); text(ax, 45, 27, '=', 'encre', 'l'); box(ax, 50, 22, 16, 10, 'autre', label='16')
text(ax, 36, 12, r'$(\sqrt{x})^2=x$', 'resultat', 'm')
text(ax, 36, 5, 'le radical disparaît', 'resultat', 's')
save(fig, '22-107')
