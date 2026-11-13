import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
for r in range(3):
    for c in range(5): box(ax,28+6*c,16+6*r,6,6,'sujet',r=0.3,lw=0.5)
box(ax,26.8,14.8,32.4,20.4,'autre',fill=False,r=0.3,lw=1.6)
text(ax,25,25,'compter : 15','autre','m',ha='right')
for r in range(3): box(ax,28,16+6*r,30,6,'varie',fill=False,r=0.3,lw=1.2)
for y,t in ((31,'5'),(25,'+ 5'),(19,'+ 5')): text(ax,62,y,t,'varie','m',ha='left')
line(ax,[(61,15.5),(70,15.5)],'varie')
text(ax,62,11,'= 15','varie','m',ha='left')
text(ax,40,6,'même nombre : 15','resultat','m',weight='bold')
save(fig,'03-011')
