import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
LV={1:0,2:1,3:1,5:1,4:2,6:2,10:2,15:2,12:3,20:3,30:3,60:4}
XP={1:44,2:24,3:44,5:64,4:14,6:34,10:54,15:74,12:24,20:44,30:64,60:44}
D60=[1,2,3,5,4,6,10,15,12,20,30,60]
def P(d,y0=8,dy=15): return (XP[d],y0+LV[d]*dy)
def edges(divs): return [(a,b) for a in divs for b in divs if b%a==0 and b!=a and not any(c!=a and c!=b and c%a==0 and b%c==0 for c in divs)]
def hasse(ax,divs,roles,hot=(),r=3.3,y0=8,dy=15):
    for a,b in edges(divs):
        (x1,y1),(x2,y2)=P(a,y0,dy),P(b,y0,dy); n=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/n,(y2-y1)/n
        on=(a,b) in hot
        line(ax,[(x1+ux*r,y1+uy*r),(x2-ux*r,y2-uy*r)],'sujet' if on else 'fixe',lw=1.6 if on else 0.8)
    for d in divs: disc(ax,*P(d,y0,dy),r,roles.get(d,'fixe'),label=str(d),size='s')
def seg(ax,p,q,r,role='fixe',lw=0.8,dash=False):
    n=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/n,(q[1]-p[1])/n
    line(ax,[(p[0]+ux*r,p[1]+uy*r),(q[0]-ux*r,q[1]-uy*r)],role,lw,dash)

fig,ax=canvas(66)
divs=[1,2,3,4,6,12]
hasse(ax,divs,{1:'sujet',2:'sujet',4:'sujet',12:'sujet'},hot=[(1,2),(2,4),(4,12)])
text(ax,28,8,'a = 1','sujet')
text(ax,36,53,'b = 12','sujet',ha='left')
text(ax,70,40,'1 < 12','resultat','l')
text(ax,68,25,'3 recouvrements','varie')
text(ax,68,18,'1, 2, 4, 12','sujet','s')
save(fig,'79-034')
