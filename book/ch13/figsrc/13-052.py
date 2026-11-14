import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y=30
f=numberline(ax,8,68,y,-4,4,every=2)
disc(ax,f(-3),y,1.5,'sujet'); disc(ax,f(3),y,1.5,'resultat')
brace(ax,f(-3),f(0),y+6,'sujet',label='3',down=False); brace(ax,f(0),f(3),y+6,'resultat',label='3',down=False)
text(ax,f(-3)+3,y+15,r'$a=-3<0$','sujet','s'); text(ax,f(3)-3,y+15,r'$-a=-(-3)=3$','resultat','s')
arrow(ax,(f(-3)+2,y-8),(f(3)-2,y-8),'varie',curve=0.3)
text(ax,f(0),y-20,'le trait change de côté','varie','s')
save(fig,'13-052')
