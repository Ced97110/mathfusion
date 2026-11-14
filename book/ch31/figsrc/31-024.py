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
quarter(ax)
A=P_(1,0); T=P_(1,TA)
line(ax,[A,(A[0],A[1]+32)],'fixe',lw=0.7)
poly(ax,[O,A,T],'sujet'); rmark(ax,A,(-1,0),(0,1))
for p in (O,A,T): dot(ax,p)
lab(ax,O,r'$O$',-3,-2.5,'sujet','m',weight='bold'); lab(ax,A,r'$A$',1,-3.5,'sujet','m',weight='bold'); lab(ax,T,r'$T$',3,2,'sujet','m',weight='bold')
text(ax,52,46,'triangle $OAT$','sujet','m',weight='bold',ha='left')
text(ax,54,38,'$O$ : le centre','encre','s',ha='left')
text(ax,54,32,'$A$ : sur le cercle','encre','s',ha='left')
text(ax,54,26,'$T$ : sur la tangente','encre','s',ha='left')
save(fig,'31-024')
