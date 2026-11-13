import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 38, 68, 'valeur en (1, 3)', 'sujet', 's')
text(ax, 68, 68, 'valeur en (3, 1)', 'autre', 's')
text(ax, 38, 62.5, r'$x=1,\ y=3$', 'sujet', 's')
text(ax, 68, 62.5, r'$x=3,\ y=1$', 'autre', 's')
rows = [(r'$x-y$', 1 - 3, 3 - 1), (r'$x^2y$', 1 * 1 * 3, 3 * 3 * 1)]
for r, (lab, a, b) in enumerate(rows):
    y = 36 - r * 26
    text(ax, 12, y + 7, lab, 'encre', 'l')
    box(ax, 28, y, 20, 14, 'sujet', label=str(a).replace('-', '−'), size='l')
    box(ax, 58, y, 20, 14, 'autre', label=str(b).replace('-', '−'), size='l')
    arrow(ax, (48.5, y + 7), (57.5, y + 7), 'varie', both=True)
    text(ax, 83, y + 7, '≠', 'limite', 'xl', weight='bold')
text(ax, 44, 4, 'x et y échangés : ça change', 'encre', 's')
save(fig, '55-067')
