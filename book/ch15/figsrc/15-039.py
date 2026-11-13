import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,4,60,r'$-x^2-4$ avec $x=3$','sujet','l',ha='left')
y=26
f=numberline(ax,6,76,y,-16,12,step=4,every=2)
for v,r,l in [(9,'sujet',r'$x^2=9$'),(-9,'varie',r'$-9$'),(-13,'resultat',r'$-13$')]:
    disc(ax,f(v),y,1.6,r); text(ax,f(v),y+5,l,r,'s')
arrow(ax,(f(9),y+8),(f(-9)+1,y+8),'varie',curve=0.4)
text(ax,f(0),49,'on change le signe','varie','s')
arrow(ax,(f(-9)-1,y+8),(f(-13)+1,y+8),'varie',curve=0.7); text(ax,f(-11),y+15,r'$-4$','varie','s')
save(fig,'15-039')
