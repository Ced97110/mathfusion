import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$5-3-2$ : deux regroupements','encre','m')
box(ax,4,38,20,9,'sujet',label=r'$5-3$'); text(ax,30,42.5,r'$-\,2$','encre','m'); text(ax,46,42.5,r'$=0$','sujet','m')
text(ax,7,24.5,r'$5-$','encre','m'); box(ax,12,20,20,9,'autre',label=r'$3-2$'); text(ax,46,24.5,r'$=4$','autre','m')
text(ax,14,34,'d’abord','sujet','s'); text(ax,22,16,'d’abord','autre','s')
text(ax,46,33.5,r'$\neq$','limite','l')
text(ax,44,6,'résultats différents','limite','m')
save(fig,'44-267')
