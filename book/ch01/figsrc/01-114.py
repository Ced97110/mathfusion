import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,16,58,12,12,'sujet',label='E',size='l',weight='bold')
text(ax,22,77,'E : « n est pair »','sujet','s')
line(ax,[(33,72),(31.5,68),(31.2,64),(31.5,60),(33,56)],'encre',lw=1.0)
line(ax,[(51,72),(52.5,68),(52.8,64),(52.5,60),(51,56)],'encre',lw=1.0)
box(ax,36,58,12,12,'varie',label='n',size='l')
text(ax,30,51.5,"l'entier qu'on met dedans",'varie','s')
f=numberline(ax,10,80,30,0,7)
for v in range(8):
    r='resultat' if v%2==0 else 'limite'
    disc(ax,f(v),37,2.2,r,lw=1.6 if v in (4,7) else 0.8)
arrow(ax,(47,57),(f(4),40),'varie',curve=0.15)
text(ax,44,19,'E(4) vraie, E(7) fausse','encre','m')
text(ax,44,11,'une affirmation par entier','encre','s')
save(fig,'01-114')
