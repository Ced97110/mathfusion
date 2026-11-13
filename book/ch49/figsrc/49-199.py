import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def shr(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L
    return (p[0]+ux*d,p[1]+uy*d),(q[0]-ux*d,q[1]-uy*d)
def link(ax,p,q,nr,role="varie",both=False,lw=1.0,curve=0.0):
    a,b=shr(p,q,nr+0.6); arrow(ax,a,b,role,lw=lw,curve=curve,both=both)
def ring(ax,cx,cy,r,labs,role,nr=3.0,start=90):
    n=len(labs); pts=[(cx+r*math.cos(math.radians(start-360*i/n)),cy+r*math.sin(math.radians(start-360*i/n))) for i in range(n)]
    for i in range(n): link(ax,pts[i],pts[(i+1)%n],nr,"varie")
    for p,l in zip(pts,labs): disc(ax,p[0],p[1],nr,role,label=l)
    return pts
fig,ax=canvas(56)
text(ax,44,50,'trois formes, trois classes','encre','m')
x=11; xsr=[]
for form,n,role in [('1+1+1',1,'sujet'),('2+1',3,'autre'),('3',2,'varie')]:
    wd=n*7+4; box(ax,x,26,wd,11,role,fill=False,dash=True)
    for i in range(n): disc(ax,x+2+3.5+i*7-0.0,31.5,2.8,role)
    text(ax,x+wd/2,41.5,form,role,'m'); text(ax,x+wd/2,21,str(n),role,'l'); xsr.append((x,x+wd)); x+=wd+6
brace(ax,xsr[0][0],xsr[-1][1],17,'fixe',label='6 permutations en tout',depth=2)
text(ax,44,4,r'$6 = 1 + 3 + 2$','resultat','l')
save(fig,'49-199')
