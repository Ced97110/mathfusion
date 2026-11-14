import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,14,40,40,16,'sujet'); text(ax,34,51,'$E$','sujet','xl'); text(ax,34,44,'corps d’arrivée','sujet','s')
box(ax,14,6,40,16,'fixe'); text(ax,34,17,'$F$','fixe','xl'); text(ax,34,10,'corps de base','fixe','s')
arrow(ax,(34,22.5),(34,40),'varie'); text(ax,46,31,'est dans','varie','s')
text(ax,72,48,'$E$ ⊇ $F$','sujet','l')
save(fig,'61-043')
