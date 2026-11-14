import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,6,70,26,0,7)
disc(ax,f(5),26,2.2,'sujet'); disc(ax,f(3),26,2.2,'limite',fill=False)
text(ax,44,54,r'$5 + x = 3$','sujet','l')
arrow(ax,(f(5)+3,33),(f(7)+2,33),'varie'); text(ax,f(6),38,'on ne peut qu’ajouter','varie','s')
arrow(ax,(f(5)-3,33),(f(3)+1,33),'limite'); text(ax,(f(5)+f(3))/2,38,r'$\times$','limite','xl')
text(ax,f(3),12,'3 est à gauche de 5','limite','s')
save(fig,'44-240')
