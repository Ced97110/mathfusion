import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx,cy,h=28,34,17
pts=[(cx-h,cy+h),(cx+h,cy+h),(cx+h,cy-h),(cx-h,cy-h)]
for i in range(4):
    p=pts[i]; q=pts[(i+1)%4]
    dx,dy=q[0]-p[0],q[1]-p[1]; n=(dx*dx+dy*dy)**0.5
    ux,uy=dx/n,dy/n
    arrow(ax,(p[0]+5*ux,p[1]+5*uy),(q[0]-5*ux,q[1]-5*uy),'sujet',lw=1.4)
for p,l in zip(pts,'1234'): disc(ax,p[0],p[1],4,'fixe',label=l)
text(ax,cx,cy,r'$T(g)$','sujet','l',weight='bold')
text(ax,68,46,r'$x \mapsto gx$','sujet','l')
text(ax,68,34,r'$g$ : quart de tour','varie','s')
text(ax,68,24,r'$S$ : les 4 sommets','fixe','s')
text(ax,44,5,r'$T(g)$ : 4 flèches de $S$ dans $S$','sujet','s')
save(fig,'49-101')
