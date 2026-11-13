import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(86)
text(ax, 36, 81, r'$O(0,\,0)$', 'sujet', 'm')
box(ax, 14, 62, 44, 10, 'sujet', label=r'$y>x+1$', size='l')
arrow(ax, (36, 62), (36, 50), 'varie'); text(ax, 40, 56, r'$x=0$ et $y=0$', 'varie', 'm', ha='left')
box(ax, 14, 40, 44, 10, 'varie', label=r'$0>0+1$', size='l')
arrow(ax, (36, 40), (36, 28), 'varie'); text(ax, 40, 34, r'calculer $0+1=1$', 'varie', 'm', ha='left')
box(ax, 14, 18, 44, 10, 'limite', label=r'$0>1$', size='l', weight='bold')
text(ax, 36, 11, 'faux', 'limite', 'l', weight='bold')
save(fig, '20-015')
