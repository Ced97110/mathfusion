import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(62)
text(ax,18,55,'liste de tous les tracés','encre','s')
for i,y in enumerate((44,36,28)): box(ax,5,y,26,6.5,'fixe',label=f'tracé {i+1}',size='s')
text(ax,18,21,'…','encre','l'); text(ax,18,9,'il y en a une infinité','limite','s')
arrow(ax,(34,33),(47,33),'varie',lw=1.3)
text(ax,66,55,'à la place','encre','s')
box(ax,49,25,35,16,'resultat'); text(ax,66.5,35,'une propriété','resultat','m'); text(ax,66.5,30,'commune à tous','resultat','m')
text(ax,66.5,17,'décrit tous les points','sujet','s'); text(ax,66.5,12,'d’un seul coup','sujet','s')
save(fig,'61-013')
