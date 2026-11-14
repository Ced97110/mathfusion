import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,2,31,38,19,'varie'); text(ax,21,44,'problème 1','varie','s'); text(ax,21,37,'partie pour le quotient','varie','s')
box(ax,2,6,38,19,'autre'); text(ax,21,19,'problème 2','autre','s'); text(ax,21,12,'noyau de « reste par 4 »','autre','s')
box(ax,52,14,34,28,'sujet'); text(ax,69,34,'multiples de 4','sujet','m'); text(ax,69,24,'0, 4, 8, 12, …','sujet','m')
arrow(ax,(40.8,40),(51.2,34),'varie'); arrow(ax,(40.8,16),(51.2,22),'autre')
save(fig,'52-014')
