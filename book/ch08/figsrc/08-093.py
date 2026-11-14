import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
x0=4
text(ax,x0,43,'2 chiffres : 0,33','autre','m',ha='left')
box(ax,x0,32,10,6,'limite',r=0.3); text(ax,x0+13,35,'erreur 1/300','limite','s',ha='left')
text(ax,x0,23,'3 chiffres : 0,333','sujet','m',ha='left')
box(ax,x0,13,1,6,'limite',r=0.1); text(ax,x0+4,16,'erreur 1/3000','limite','s',ha='left')
arrow(ax,(66,34),(66,18),'varie'); text(ax,76,26,'10 fois\nmoins','varie','s')
save(fig,'08-093')
