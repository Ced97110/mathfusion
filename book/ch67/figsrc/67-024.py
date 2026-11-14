import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 8, 80, 64, 'fixe')
text(ax, 44, 66, r'$F$ : 4 éléments', 'fixe', 'm')
box(ax, 6, 20, 38, 26, 'sujet', fill=True)
for i, l in enumerate(['0', '1']):
    box(ax, 9 + 17 * i, 26, 14, 12, 'sujet', label=l)
for i, l in enumerate([r'$\alpha$', r'$\alpha+1$']):
    box(ax, 50 + 17 * i, 26, 14, 12, 'varie', label=l, size='s')
arrow(ax, (33, 46), (16, 46), 'sujet', curve=0.6)
text(ax, 25, 56, r'$1+1=0$', 'sujet', 'm')
text(ax, 25, 14, 'corps premier : 0 et 1', 'sujet', 's')
text(ax, 66, 18, 'pas des sommes de 1', 'varie', 's')
save(fig, '67-024')
