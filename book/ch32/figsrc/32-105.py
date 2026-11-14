import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
top=[(3,18,'cos² x'),(28,18,'2 cos x'),(53,8,'1')]
for k,(x,w_,lab) in enumerate(top):
    box(ax,x,34,w_,9,'sujet',label=lab)
    box(ax,x,10,w_,9,'resultat',label=('u²','2u','1')[k])
    arrow(ax,(x+w_/2,34),(x+w_/2,19),'varie')
for xp in (24.5,49.5):
    text(ax,xp,38.5,'+','encre','m'); text(ax,xp,14.5,'+','encre','m')
text(ax,72,38.5,'= 0','encre','m'); text(ax,72,14.5,'= 0','encre','m')
text(ax,75,26.5,'u = cos x','varie','m')
save(fig,'32-105')
