import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'dans les restes par 6', 'autre', 's')
box(ax, 4, 50, 36, 12, 'autre', label=r'$\bar2\times\bar3$'); box(ax, 48, 50, 36, 12, 'autre', label=r'$=\bar0$')
box(ax, 4, 14, 36, 12, 'sujet', label=r'$2\times3=6$'); box(ax, 48, 14, 36, 12, 'sujet', label=r'$\in(6)$')
arrow(ax, (22, 50), (22, 26.5), 'varie', both=True); arrow(ax, (66, 50), (66, 26.5), 'varie', both=True)
text(ax, 44, 38, 'se traduit', 'varie', 's')
text(ax, 44, 7, 'dans les entiers', 'sujet', 's')
save(fig, '52-121')
