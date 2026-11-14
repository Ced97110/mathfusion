import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 46, 38, 18, 'sujet', label=None)
text(ax, 21, 58, r'$\mathbb{Z}/4\mathbb{Z}$', 'sujet', 'l'); text(ax, 21, 51, r'quotient par 4$\mathbb{Z}$', 'sujet', 's')
box(ax, 48, 46, 38, 18, 'autre', label=None)
text(ax, 67, 58, 'résidus', 'autre', 'm'); text(ax, 67, 51, 'modulo 4', 'autre', 'm')
text(ax, 44, 55, '=', 'encre', 'xl')
arrow(ax, (21, 45), (30, 32), 'sujet'); arrow(ax, (67, 45), (58, 32), 'autre')
for i in range(4):
    box(ax, 8 + i * 19.5, 16, 17, 14, 'resultat', label=r'$\bar{%d}$' % i, size='l')
text(ax, 44, 8, 'les mêmes 4 classes', 'resultat', 's')
save(fig, '52-080')
