import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y=16
f=numberline(ax,8,68,y,-2,5,every=1)
arrow(ax,(f(0),y+5),(f(3),y+5),'sujet'); text(ax,f(1.5),y+8,'3 pas à droite','sujet','s')
line(ax,[(f(3),y+5),(f(3),y+14)],'fixe',dash=True)
arrow(ax,(f(3),y+14),(f(1),y+14),'varie'); text(ax,f(2),y+17.5,'2 pas à gauche','varie','s')
disc(ax,f(0),y,1.5,'fixe'); disc(ax,f(1),y,1.5,'resultat')
text(ax,f(0)-3,y+8,'départ','fixe','s'); text(ax,f(1),y-8,'arrivée','resultat','s')
save(fig,'13-054')
