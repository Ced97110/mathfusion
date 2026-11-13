import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(90)
rows=[(72,2,'sujet',r'$2\mathbb{Z}$'),(50,3,'varie',r'$3\mathbb{Z}$'),(28,6,'resultat',r'$6\mathbb{Z}$')]
for y,s,role,lab in rows:
    f=numberline(ax,8,70,y,-12,12,labels=(s==6),every=6,arrow_right=True,size='s')
    for v in range(-12,13):
        if v%s==0: disc(ax,f(v),y,1.3,role)
    text(ax,4,y+7,lab,role,'m',ha='left')
for v in (-12,-6,0,6,12):
    line(ax,[(f(v),74),(f(v),26)],'fixe',lw=0.5,dash=True)
text(ax,44,8,'multiples de 6 : bleus et orange','encre','s')
save(fig,'46-111')
