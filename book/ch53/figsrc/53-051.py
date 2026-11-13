import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 5 * 21 == 105 == 4 * 26 + 1

fig, ax = canvas(52)
yb, h = 30, 13
box(ax, 3, yb, 14, h, 'sujet', label=r'$p$')
box(ax, 37, yb, 14, h, 'varie', label=r'$5p$')
box(ax, 71, yb, 14, h, 'resultat', label=r'$p$')
arrow(ax, (18, yb + h / 2), (36, yb + h / 2), 'varie')
arrow(ax, (52, yb + h / 2), (70, yb + h / 2), 'resultat')
text(ax, 27, yb + h / 2 + 3.5, r'$\times\,5$', 'varie', 'm')
text(ax, 61, yb + h / 2 + 3.5, r'$\times\,21$', 'resultat', 'm')
text(ax, 44, 26, r'$\times\,21$ défait $\times\,5$', 'encre', 's')
box(ax, 10, 6, 68, 12, 'resultat', label=r'$5 \times 21 = 105 = 4 \times 26 + 1$')
save(fig, '53-051')
