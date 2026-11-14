import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74); y=34
f=numberline(ax,8,80,y,-60,60,step=12,labels=False,arrow_right=False)
line(ax,[(f(0),y-9),(f(0),y+17)],'fixe',dash=True)
text(ax,f(0),y-12,'miroir en 0','fixe','s')
for v,r in ((24,'sujet'),(56,'autre'),(-24,'sujet'),(-56,'autre')):
    disc(ax,f(v),y,1.8,r); text(ax,f(v),y-4.5,f'${v}$',r,'s')
arrow(ax,(f(24),y+4),(f(-24),y+4),'varie',curve=0.3); arrow(ax,(f(56),y+4),(f(-56),y+4),'varie',curve=0.3)
text(ax,44,y+25,'la symétrie place les points','varie','s')
text(ax,44,y-22,r'$-24>-56$','resultat','l')
text(ax,44,y-29,'dit où sont les points','resultat','s')
save(fig,'17-072')
