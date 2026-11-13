import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
TH=math.radians(35); CO,SI,TA=math.cos(TH),math.sin(TH),math.tan(TH)
R=30.0; O=(10.0,10.0)
def P_(a,b): return (O[0]+a*R,O[1]+b*R)
def arcpts(c,r,a0,a1,n=60): return [(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
def quarter(ax,ext=22):
    line(ax,arcpts(O,R,0,90),'fixe')
    arrow(ax,O,(O[0]+R+ext,O[1]),'fixe',lw=0.6); arrow(ax,O,(O[0],O[1]+R+8),'fixe',lw=0.6)
def rmark(ax,p,d1,d2,s=2.4):
    a=(p[0]+d1[0]*s,p[1]+d1[1]*s); c=(p[0]+d2[0]*s,p[1]+d2[1]*s); b=(a[0]+d2[0]*s,a[1]+d2[1]*s)
    line(ax,[a,b,c],'fixe',lw=0.7)
def dot(ax,p,role='encre',r=0.9): ax.add_patch(Circle(p,r,fc=COL[role],ec=COL[role],zorder=6))
def lab(ax,p,s,dx,dy,role='encre',size='m',**k): text(ax,p[0]+dx,p[1]+dy,s,role,size,**k)
fig,ax=canvas(54)
u=44.0; O3=(8.0,8.0)
A=(O3[0]+u,8); T=(A[0],8+TA*u); Pp=(O3[0]+u*CO,8+u*SI)
poly(ax,[O3,A,T],'fixe'); rmark(ax,A,(-1,0),(0,1))
line(ax,[O3,Pp],'sujet',lw=2.2); line(ax,[Pp,T],'varie',lw=2.2)
for p in (O3,A,T,Pp): dot(ax,p)
lab(ax,O3,r'$O$',-3,-2.5); lab(ax,A,r'$A$',1,-3.5); lab(ax,T,r'$T$',2.5,2); lab(ax,Pp,r'$P$',-2.5,3)
text(ax,A[0]+2,(A[1]+T[1])/2-2,'0,7002','fixe','s',ha='left')
text(ax,(O3[0]+Pp[0])/2-3,(O3[1]+Pp[1])/2+4,'$OP=1$','sujet','s')
text(ax,Pp[0]+4,Pp[1]+9,'$PT\\approx 0{,}2208$','varie','s') if False else None
text(ax,(Pp[0]+T[0])/2-4,(Pp[1]+T[1])/2+4.5,'0,2208','varie','s')
text(ax,76,42,'$OT\\approx 1{,}2208$','resultat','s') if False else None
text(ax,72,44,r'$OT\approx 1{,}2208$','resultat','s')
text(ax,72,36,r'$OT^2\approx 1{,}4903$','encre','s')
text(ax,72,30,r'$1+0{,}4903$','encre','s')
save(fig,'31-030')
