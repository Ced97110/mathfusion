import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y=16
f=numberline(ax,8,68,y,-6,4,every=1)
arrow(ax,(f(0),y+5),(f(-5),y+5),'varie'); text(ax,f(-2.5),y+8,r'$-5$ : 5 pas à gauche','varie','s')
line(ax,[(f(-5),y+5),(f(-5),y+13)],'fixe',dash=True)
arrow(ax,(f(-5),y+13),(f(-2),y+13),'sujet'); text(ax,f(-3.5),y+16.5,r'$+3$ : 3 pas à droite','sujet','s')
disc(ax,f(0),y,1.5,'fixe'); disc(ax,f(-2),y,1.7,'resultat')
text(ax,f(0)+4,y+8,'départ','fixe','s'); text(ax,f(-2),y-8,r'$(-5)+3=-2$','resultat','s')
save(fig,'13-055')
