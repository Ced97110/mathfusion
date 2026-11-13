import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cx,cy,R=26,38,22
P=[(cx+R*math.cos(math.radians(90+60*i)),cy+R*math.sin(math.radians(90+60*i))) for i in range(6)]
poly(ax,P,'fixe')
poly(ax,[P[0],P[2],P[4]],'sujet')
for p in P: disc(ax,p[0],p[1],1.3,'fixe')
arrow(ax,(P[1][0]+1,P[1][1]-0.6),(P[4][0]-1,P[4][1]+0.6),'varie',both=True,lw=1.2)
text(ax,cx+3,cy-3,'H','varie','m')
text(ax,66,52,'K : 6 symétries du triangle','sujet','s')
text(ax,66,40,'H : demi-tour (2)','varie','s')
text(ax,44,8,'2 × 6 = 12 symétries','resultat','l')
save(fig,'45-245')
