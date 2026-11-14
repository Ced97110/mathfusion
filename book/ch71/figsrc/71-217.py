import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y0 = 28
poly(ax, [(6, y0), (20, y0), (20, y0+14), (6, y0+14)], 'sujet')
poly(ax, [(46, y0), (74, y0), (74, y0+7), (46, y0+7)], 'resultat')
arrow(ax, (6, y0-1.5), (20, y0-1.5), 'sujet'); arrow(ax, (46, y0-1.5), (74, y0-1.5), 'resultat')
text(ax, 13, y0-5.5, r'$(1,\ 0)$', 'sujet', 's'); text(ax, 60, y0-5.5, r'$(2,\ 0)$', 'resultat', 's')
text(ax, 2.5, y0+7, r'$(0,\ 1)$', 'sujet', 's', ha='left'); ax.texts[-1].set_x(13); ax.texts[-1].set_ha('center')
text(ax, 60, y0+11, r'$(0,\ \frac{1}{2})$', 'resultat', 's')
text(ax, 13, y0+19.5, 'aire = 1', 'sujet', 's'); text(ax, 60, y0+19.5, 'aire = 1', 'resultat', 's')
arrow(ax, (24, y0+7), (42, y0+7), 'varie'); text(ax, 33, y0+11, r'$\times 2,\ \div 2$', 'varie', 's')
text(ax, 44, 12, r'aire orientée conservée : $1\to1$', 'resultat', 's')
text(ax, 44, 5, r'longueur de (1, 0) : $1\to2$', 'limite', 's')
save(fig, '71-217')
