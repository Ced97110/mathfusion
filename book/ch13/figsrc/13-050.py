import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
y=22
f=numberline(ax,8,68,y,-4,4,every=2)
disc(ax,f(-3),y,1.5,'sujet'); disc(ax,f(3),y,1.5,'resultat')
text(ax,f(-3)+1,y+5,r'$a=-3$','sujet','s'); text(ax,f(3)-1,y+5,r'$-a=3$','resultat','s')
arrow(ax,(f(-3)+2,y+10),(f(3)-2,y+10),'varie',curve=-0.3)
text(ax,f(0),y+20,'change de côté','varie','s')
brace(ax,f(-3),f(0),y-6.5,label='3'); brace(ax,f(0),f(3),y-6.5,label='3')
save(fig,'13-050')
