import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(80)
for cx,step,role,n,title in [(22,4,'sujet',3,r'$a=4$'),(66,5,'autre',12,r'$a=5$')]:
    vis={(step*i)%12 for i in range(12)}
    for k in range(12):
        p=cp(cx,48,13,12,k); v=k in vis
        disc(ax,p[0],p[1],1.8 if v else 0.8,role if v else 'fixe',fill=v)
    text(ax,cx,72,title,role,'m')
    text(ax,cx,22,f'{n} éléments',role,'m')
    text(ax,cx,12,rf'$o({step})={n}$',role,'m')
text(ax,44,48,'=','resultat','l')
save(fig,'46-110')
