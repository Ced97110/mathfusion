import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
box(ax, 2, 62, 18, 12, 'sujet', label=r'$x$', size='l'); box(ax, 28, 62, 58, 12, 'sujet', label=r'$y_1=mx+b$', size='l')
arrow(ax, (20, 68), (28, 68), 'sujet')
box(ax, 2, 40, 18, 12, 'varie', label=r'$x+1$', size='m'); box(ax, 28, 40, 58, 12, 'varie', label=r'$y_2=mx+m+b$', size='l')
arrow(ax, (20, 46), (28, 46), 'varie')
text(ax, 57, 57, r'développer $m(x+1)+b$', 'varie', 's')
arrow(ax, (57, 38), (57, 28), 'resultat')
box(ax, 14, 12, 60, 15, 'resultat', label=r'$y_2-y_1=m$', size='l')
text(ax, 44, 5, r'cas : $9-7=2$', 'fixe', 's')
save(fig, '19-089')
