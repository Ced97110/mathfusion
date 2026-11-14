import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(70)
for y,s,role in [(48,1,'varie'),(22,2,'autre')]:
    f=numberline(ax,8,70,y,0,8,labels=(s==2),every=2,arrow_right=True)
    for v in range(0,9,s):
        disc(ax,f(v),y,1.4,role if v else 'fixe')
        if v:
            p,q=sh((f(v-s),y+1.5),(f(v),y+1.5),0.6); arrow(ax,p,q,role,lw=0.7,curve=-0.5)
    text(ax,4,y+9,f'+{s} à chaque pas',role,'s',ha='left')
text(ax,8,38,'0 : le neutre','fixe','s',ha='left')
text(ax,74,56,'jamais 0','limite','m',ha='right')
text(ax,74,13,r'$o(1)=\infty$','sujet','m',ha='right')
save(fig,'46-098')
