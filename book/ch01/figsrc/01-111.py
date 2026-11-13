import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
line(ax,[(10,72),(24,67),(10,62)],'sujet',lw=2.2*1.0)
line(ax,[(26,67),(40,67)],'sujet',lw=0.6)
text(ax,52,67,'plus grand que','sujet','m')
line(ax,[(10,57.5),(24,57.5)],'varie',lw=2.2)
line(ax,[(26,57.5),(36,57.5)],'varie',lw=0.6)
text(ax,54,57.5,'ou égal : le cas limite','varie','m')
text(ax,44,48,'témoin de 16 500 : 5','encre','m')
for v,x in zip((4,5,6,7),(36,46,56,66)):
    if v==5: text(ax,x,40,'5','varie','m',weight='bold')
    else: text(ax,x,40,str(v),'fixe','m')
xs=(31.5,41.5,51.5,61.5)
text(ax,14,30,'témoin ≥ 5','sujet','l')
for i,x in enumerate(xs):
    if i==0: box(ax,x,26.5,9,7,'fixe',fill=False)
    else: box(ax,x,26.5,9,7,'resultat')
box(ax,xs[1],26.5,9,7,'varie',fill=False,lw=1.6)
text(ax,79,30,'17 000','resultat','m')
text(ax,14,18,'témoin > 5','limite','l')
for i,x in enumerate(xs):
    box(ax,x,14.5,9,7,'fixe' if i==0 else ('limite' if i==1 else 'resultat'))
text(ax,79,18,'16 000','limite','m')
save(fig,'01-111')
