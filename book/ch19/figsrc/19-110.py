import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, b, r in [(40, r'$+\,1$', 'sujet'), (16, r'$-\,5$', 'autre')]:
    text(ax, 6, y + 6, r'$y=$', r, 'l')
    box(ax, 14, y, 22, 12, 'sujet', label=r'$2x$', size='l')
    box(ax, 56, y, 28, 12, 'varie', label=b, size='l')
text(ax, 25, 62, 'même nombre', 'sujet', 's'); text(ax, 70, 62, 'seul change', 'varie', 's')
text(ax, 25, 33, '=', 'resultat', 'l')
text(ax, 70, 33, '≠', 'varie', 'l')
text(ax, 44, 4, 'même pente : parallèles', 'resultat', 'm')
save(fig, '19-110')
