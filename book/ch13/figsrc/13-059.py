import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(98)
y=68
f=numberline(ax,6,66,y,-9,12,labels=False)
arrow(ax,(f(0),y+5),(f(3),y+5),'sujet'); text(ax,f(1.5)+4,y+8,'3','sujet','s')
line(ax,[(f(3),y+5),(f(3),y+11)],'fixe',dash=True)
arrow(ax,(f(3),y+11),(f(-8),y+11),'varie',lw=2.2); text(ax,f(-2.5),y+14.5,'11','varie','s')
disc(ax,f(-8),y,1.7,'resultat'); text(ax,f(0),y-4.5,'0','fixe','s')
text(ax,50,y-9,r'$3+(-11)=-8$','resultat','s'); text(ax,44,y-15,'la plus longue va à gauche','encre','s')
y=26
g=numberline(ax,6,66,y,-9,12,labels=False)
arrow(ax,(g(0),y+5),(g(11),y+5),'sujet',lw=2.2); text(ax,g(5.5),y+8,'11','sujet','s')
line(ax,[(g(11),y+5),(g(11),y+11)],'fixe',dash=True)
arrow(ax,(g(11),y+11),(g(8),y+11),'varie'); text(ax,g(9.5),y+14.5,'3','varie','s')
disc(ax,g(8),y,1.7,'resultat'); text(ax,g(0),y-4.5,'0','fixe','s')
text(ax,50,y-9,r'$11+(-3)=8$','resultat','s'); text(ax,44,y-15,'la plus longue va à droite','encre','s')
save(fig,'13-059')
