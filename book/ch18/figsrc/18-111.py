import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,36,46,10,'fixe',label=r'$x^2+5x+6=0$',size='m')
box(ax,2,12,46,10,'fixe',label=r'$x^2+5x=-6$',size='m')
arrow(ax,(25,36),(25,22),'varie'); text(ax,30,29,r'retirer 6','varie','s',ha='left')
box(ax,56,12,13,10,'sujet',label=r'$x^2$',size='m'); box(ax,71,12,13,10,'varie',label=r'$5x$',size='m')
arrow(ax,(48,17),(56,17),'fixe')
text(ax,70,28,r'$x$ dans 2 termes','limite','s'); text(ax,70,5,'impossible de réunir','limite','s')
save(fig,'18-111')
