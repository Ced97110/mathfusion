import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(68)
O=(30,31); R=27; th=math.radians(35); c,s=math.cos(th),math.sin(th)
P=(O[0]+R*c,O[1]+R*s); A=(O[0]+R,O[1]); Hh=(P[0],O[1]); B=(O[0],O[1]+R)
T=(O[0]+R,O[1]+R*s/c); S=(O[0]+R*c/s,O[1]+R)
disc(ax,*O,R,'fixe',fill=False,lw=0.7)
line(ax,[(O[0]-R-2,O[1]),(O[0]+R+6,O[1])],'fixe',lw=0.5); line(ax,[(O[0],O[1]-R-2),(O[0],O[1]+R+4)],'fixe',lw=0.5)
line(ax,[A,T],'resultat',lw=1.8); line(ax,[B,S],'resultat',lw=1.8,dash=True)
line(ax,[O,T],'fixe',lw=0.6,dash=False)
line(ax,[T,S],'fixe',lw=0.6)
line(ax,[O,Hh],'sujet',lw=1.8); line(ax,[Hh,P],'varie',lw=1.8)
nx,ny=-s,c
def dim(p,q,off,role):
    a=(p[0]+nx*off,p[1]+ny*off); b=(q[0]+nx*off,q[1]+ny*off); arrow(ax,a,b,role,lw=0.9,both=True)
    return ((a[0]+b[0])/2,(a[1]+b[1])/2)
dim(O,T,-2.6,'autre'); text(ax,O[0]+0.62*(T[0]-O[0])+s*5.4,O[1]+0.62*(T[1]-O[1])-c*5.4,'sec','autre','s')
m=dim(O,S,3.2,'autre'); text(ax,m[0]+nx*4.6,m[1]+ny*4.6,'cosec','autre','s')
text(ax,(O[0]+Hh[0])/2,O[1]-3,'cos','sujet','s')
text(ax,Hh[0]-1.6,O[1]+3.2,'sin','varie','s',ha='right')
text(ax,A[0]+3.5,(A[1]+T[1])/2-3,'tan','resultat','s')
text(ax,(B[0]+S[0])/2,B[1]+3,'cotan','resultat','s')
disc(ax,*P,0.8,'encre'); text(ax,P[0]+2.4,P[1]+2.4,'P','encre','s')
text(ax,A[0]+2.5,A[1]-3,'A','encre','s'); text(ax,P[0]+2.0,P[1]+3.0,'P','encre','s') if False else None
text(ax,O[0]-3,O[1]-3,'O','encre','s')
r=7; line(ax,[(O[0]+r*math.cos(math.radians(a)),O[1]+r*math.sin(math.radians(a))) for a in range(0,36,3)],'encre',lw=0.8)
text(ax,O[0]+10,O[1]+2.6,r'$\theta$','encre','s')
save(fig,'31-011')
