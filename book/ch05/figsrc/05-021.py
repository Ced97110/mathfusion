import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
f=lambda v: 14+(v+12)*60/42
text(ax,24,75,'pas de 12','sujet','m'); text(ax,66,75,'pas de 18','autre','m')
data=[(56,r'$12\times 1+18\times 1=30$',[(0,12,'sujet'),(12,30,'autre')],30),
      (34,r'$12\times 2+18\times 0=24$',[(0,12,'sujet'),(12,24,'sujet')],24),
      (12,r'$12\times(-1)+18\times 1=6$',[(0,-12,'sujet'),(-12,6,'autre')],6)]
for y,t,steps,end in data:
    line(ax,[(f(-12),y),(f(30),y)],'fixe')
    ax.plot([f(0)]*2,[y-1.2,y+1.2],color=COL['fixe'],lw=0.8)
    text(ax,f(0),y-4,'0','fixe','s')
    for a,b,r in steps:
        arrow(ax,(f(a),y),(f(b),y),r,curve=-0.4 if b>a else 0.4)
    disc(ax,f(end),y,1.4,'resultat')
    text(ax,44,y+13,t,'encre','m')
save(fig,'05-021')
