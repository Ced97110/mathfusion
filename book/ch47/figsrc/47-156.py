import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, role, l in [(13, 'varie', 'S'), (39, 'varie', 'S'), (71, 'resultat', 'R')]:
    box(ax, x - 7, 50, 14, 10, role, label=l, size='l')
text(ax, 26, 55, '·', 'encre', 'l'); text(ax, 55, 55, '=', 'encre', 'l')
box(ax, 4, 26, 38, 11, 'varie', label=r'$s \cdot s = 1$', size='m'); box(ax, 46, 26, 38, 11, 'varie', label=r'$s \cdot rs = r^3$', size='m')
arrow(ax, (23, 37.5), (63, 49.5), 'resultat'); arrow(ax, (65, 37.5), (69, 49.5), 'resultat')
text(ax, 23, 20, 'même retournement', 'fixe', 's'); text(ax, 65, 20, 'retournements différents', 'fixe', 's')
box(ax, 4, 3, 80, 9, 'resultat', label='dans les deux cas : une rotation', size='s')
save(fig, '47-156')
