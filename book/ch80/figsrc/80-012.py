import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
line(ax,[(10,8),(54,52)],'sujet',lw=1.3); line(ax,[(10,17),(45,52)],'autre',lw=1.3)
text(ax,56,52,r'$x-y=0$','sujet','m',ha='left')
text(ax,43,56,r'$x-y=-1$','autre','m',ha='right')
text(ax,66,34,'0 = 1 : faux','limite','m')
text(ax,66,26,'aucune solution','limite','m')
text(ax,66,15,'droites parallèles :\naucun point commun','encre','s')
save(fig,'80-012')
