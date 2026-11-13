import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
y=lambda v:70-(v-1)*11
f=lambda v:(3*v)%7
xl,xr,r=22,66,1.8
box(ax,8,12,26,64,'sujet',fill=False,lw=1.0); box(ax,54,12,28,64,'fixe',fill=False,lw=1.0)
text(ax,21,82,'① colonne x','sujet','m'); text(ax,68,82,'② colonne de droite','fixe','m')
for v in range(1,7):
    if v not in (4,5): link((xl,y(v)),(xr,y(f(v))),r,r,'fixe',0.8)
link((xl,y(4)),(xr,y(5)),r,r,'varie',1.6)
link((xl,y(5)),(xr,y(1)),r,r,'resultat',1.6)
for v in range(1,7):
    disc(ax,xl,y(v),r,'sujet'); disc(ax,xr,y(v),r,'fixe')
text(ax,15,y(4),'4','sujet'); text(ax,15,y(5),'5','sujet')
text(ax,75,y(5),'5','varie'); text(ax,75,y(1),'1','resultat')
text(ax,22,5,'③ flèche suivie','varie','m'); text(ax,66,5,'④ flèche qui arrive sur 1','resultat','m')
for (px,py),s,rl in (((44,y(4)+(y(5)-y(4))/2+0.5),'3','varie'),((44,y(5)+(y(1)-y(5))/2),'4','resultat')):
    tt=text(ax,px,py,s,rl,'l',weight='bold'); tt.set_bbox(dict(fc='white',ec=COL[rl],lw=0.8,boxstyle='circle,pad=0.25'))
save(fig,'51-225')
