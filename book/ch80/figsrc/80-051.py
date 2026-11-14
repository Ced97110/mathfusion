import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,4,6,80,44,'varie',label=None)
text(ax,44,45,'droite de la figure (cercle)','varie','s')
text(ax,44,38,'{000, 110, 101, 011}','varie','m')
box(ax,14,10,60,20,'sujet')
text(ax,44,24,'point 110 : {000, 110}','sujet','m')
text(ax,44,15,'contenu dans l’ensemble du cercle','sujet','s')
save(fig,'80-051')
