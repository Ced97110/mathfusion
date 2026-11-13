import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
y=32
f=numberline(ax,6,82,y,0,13,1,labels=False,arrow_right=False)
for v in (0,5,7,12): text(ax,f(v),28,str(v),'fixe','s')
def dot(v,r,role):
    ax.add_patch(Circle((f(v),y),r,fc=FILL[role] if role=='sujet' else COL[role],ec=COL[role],lw=0.8,zorder=4))
for v in (5,7,12): dot(v,1.4,'sujet')
for v in range(5): dot(v,1.0,'resultat')
ax.add_patch(Circle((f(5),y),2.3,fc='none',ec=COL['resultat'],lw=0.9,zorder=4.5))
text(ax,66,20,'S = 5, 7, 12','sujet','m')
text(ax,21,20,'M = 0 à 5 : ≤ 5, 7 et 12','resultat','s')
text(ax,3,38,'départ','resultat','s',ha='left')
def rad(p,q,top):
    d=math.hypot(q[0]-p[0],q[1]-p[1]); return -2*(top-(p[1]+q[1])/2)/d
for i in range(5):
    p=(f(i)+0.9,y+0.7); q=(f(i+1)-0.9,y+0.7)
    if i==4: q=(f(5)-1.9,y+1.3)
    arrow(ax,p,q,'varie',lw=1.2,curve=rad(p,q,y+2.5))
p=(f(5)+1.9,y+1.3); q=(f(6)-0.3,y+1.3)
ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-',lw=1.0,ls='--',color=COL['limite'],connectionstyle=f'arc3,rad={rad(p,q,36)}',zorder=4,shrinkA=0,shrinkB=0))
mx=(p[0]+q[0])/2; d=1.0
line(ax,[(mx-d,36-d),(mx+d,36+d)],'limite',lw=1.1); line(ax,[(mx-d,36+d),(mx+d,36-d)],'limite',lw=1.1)
text(ax,22,44,r'un pas : $m$, puis $m+1$','varie','m',weight='bold')
text(ax,60,42,'arrêt : 5 est dans S','limite','s')
text(ax,44,11,'sans plus petit : M sans fin','limite','s')
text(ax,44,5,'M = tous : 5 + 1 ≤ 5, faux','limite','s')
save(fig,'01-153')
