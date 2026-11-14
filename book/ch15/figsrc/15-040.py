import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,4,60,r'$(-x)^2-4$ avec $x=3$','autre','l',ha='left')
y=26
f=numberline(ax,6,76,y,-16,12,step=4,every=2)
for v,r,l in [(-3,'autre',r'$-3$'),(9,'autre',r'$9$'),(5,'resultat',r'$5$'),(-13,'limite',r'$-13$')]:
    disc(ax,f(v),y,1.6,r); text(ax,f(v),y+5,l,r,'s')
arrow(ax,(f(-3),y+8),(f(9),y+8),'varie',curve=-0.4)
text(ax,f(3),47,r'$\times(-3)$','varie','s')
arrow(ax,(f(9)-1,y+8),(f(5)+1,y+8),'varie',curve=-0.9); text(ax,f(7),y+15,r'$-4$','varie','s')
text(ax,3,y+15,r'sans ( ) : $-13$','limite','s',ha='left')
save(fig,'15-040')
