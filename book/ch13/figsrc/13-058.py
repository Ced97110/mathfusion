import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
y=70
f=numberline(ax,8,68,y,-9,5,labels=False)
arrow(ax,(f(0),y+5),(f(3),y+5),'sujet'); text(ax,f(1.5)+3,y+8,'3 à droite','sujet','s')
line(ax,[(f(3),y+5),(f(3),y+13)],'fixe',dash=True)
arrow(ax,(f(3),y+13),(f(-8),y+13),'varie'); text(ax,f(-2.5),y+16.5,'11 pas à gauche','varie','s')
disc(ax,f(-8),y,1.7,'resultat'); text(ax,f(0),y-4.5,'0','fixe','s')
text(ax,30,y-9,r'$3+(-11)=-8$','resultat','s'); text(ax,36,y-15,r'$11-3=8$, signe $-$','encre','s')
y=26
g=numberline(ax,8,68,y,-6,6,labels=False)
arrow(ax,(g(0),y+5),(g(5),y+5),'sujet'); text(ax,g(2.5),y+8,'5 à droite','sujet','s')
line(ax,[(g(5),y+5),(g(5),y+13)],'fixe',dash=True)
arrow(ax,(g(5),y+13),(g(0),y+13),'varie'); text(ax,g(2.5),y+16.5,'5 à gauche','varie','s')
disc(ax,g(0),y,1.7,'resultat'); text(ax,g(0),y-6,r'$5+(-5)=0$','resultat','s')
save(fig,'13-058')
