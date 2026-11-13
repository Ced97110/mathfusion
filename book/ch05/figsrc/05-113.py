import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
text(ax,44,83,'un seul sens : nombres différents','limite','s')
y=66
f=numberline(ax,8,72,y,0,12,step=1,labels=False)
disc(ax,f(6),y,3.2,'sujet',label='6')
disc(ax,f(12),y,3.4,'autre',label='12')
arrow(ax,(f(6)+2,y+2.5),(f(12)-2,y+2.5),'resultat',curve=-0.45)
text(ax,56,79,r'$6\times 2=12$ : 6 divise 12','resultat','s') if False else None
text(ax,40,77,r'$6\times 2=12$ : 6 divise 12','resultat','s')
arrow(ax,(f(12)-2,y-2.5),(f(6)+2,y-2.5),'limite',curve=-0.45)
text(ax,40,53,'12 ne divise pas 6 : 6 < 12','limite','s')
line(ax,[(4,46),(84,46)],'fixe',dash=True)
text(ax,44,42,'deux sens : nombres égaux','resultat','s')
yb=22
disc(ax,16,yb,4.2,'sujet',label='a')
disc(ax,72,yb,4.2,'sujet',label='b')
arrow(ax,(20.6,yb+1.5),(67.4,yb+1.5),'resultat',curve=-0.18)
arrow(ax,(67.4,yb-1.5),(20.6,yb-1.5),'resultat',curve=-0.18)
text(ax,44,yb+10.5,r'$a\mid b$','resultat','s')
text(ax,44,yb-10.5,r'$b\mid a$','resultat','s')
text(ax,44,yb,r'$a=b$','resultat','xl',weight='bold')
save(fig,'05-113')
