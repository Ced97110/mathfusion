import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
f=lambda v: 4+2.1*v
yA,yB=40,22
line(ax,[(f(0),yA),(f(36),yA)],'fixe'); line(ax,[(f(0),yB),(f(35),yB)],'fixe')
ax.add_patch(Rectangle((f(35),yB),f(36)-f(35),yA-yB,fc=FILL['resultat'],ec=COL['resultat'],lw=0.6,zorder=1))
for k in range(5):
    disc(ax,f(9*k),yA,1.0,'sujet')
    if k<4: arrow(ax,(f(9*k)+0.5,yA+1.2),(f(9*k+9)-0.5,yA+1.2),'sujet',curve=-0.45)
disc(ax,f(36),yA,1.0,'sujet')
for k in range(6):
    disc(ax,f(7*k),yB,1.0,'autre')
    if k<5: arrow(ax,(f(7*k)+0.5,yB-1.2),(f(7*k+7)-0.5,yB-1.2),'autre',curve=0.45)
text(ax,44,50,'pas de 9 : 9 × 4 = 36','sujet','m')
text(ax,44,13,'pas de 7 : 7 × 5 = 35','autre','m')
text(ax,f(35)-2,31,'écart : 1','resultat','m',ha='right')
text(ax,44,4.5,'un diviseur commun divise 1','encre','m')
save(fig,'05-158')
