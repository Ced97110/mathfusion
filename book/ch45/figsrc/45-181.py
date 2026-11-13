import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(74)
cx,cy,rx,ry=44,37,30,24; bw,bh=12,6.4
P=[(0,0),(1,1),(0,2),(1,0),(0,1),(1,2)]
ang=[math.radians(90-60*i) for i in range(6)]
C=[(cx+rx*math.cos(a),cy+ry*math.sin(a)) for a in ang]
for i,(p,c) in enumerate(zip(P,C)):
    box(ax,c[0]-bw/2,c[1]-bh/2,bw,bh,'sujet' if i==0 else 'fixe',label=rf'$({p[0]},{p[1]})$',size='s')
    a=ang[i]; q=(c[0]+10*math.cos(a),c[1]+7*math.sin(a))
    text(ax,q[0],q[1],'0 et 6' if i==0 else str(i),'resultat' if i==0 else 'varie','s')
def edge(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    t=min(bw/2/abs(dx) if dx else 9, bh/2/abs(dy) if dy else 9)+0.05
    return (a[0]+dx*t,a[1]+dy*t)
for i in range(6):
    a,b=C[i],C[(i+1)%6]
    arrow(ax,edge(a,b),edge(b,a),'varie')
text(ax,cx,cy,'ordre 6','resultat','l',weight='bold')
save(fig,'45-181')
