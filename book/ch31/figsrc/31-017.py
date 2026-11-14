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
fig,ax=canvas(52)
quarter(ax)
B=P_(0,1); S=P_(1/TA,1); Pp=P_(CO,SI)
line(ax,[(O[0]-3,B[1]),(S[0]+7,B[1])],'fixe',lw=0.8)
line(ax,[O,S],'sujet',lw=1.4); line(ax,[B,S],'varie',lw=1.6)
for p in (O,B,Pp): dot(ax,p)
dot(ax,S,'sujet',1.3)
lab(ax,O,r'$O$',-3,-2.5); lab(ax,B,r'$B$',-3,3); lab(ax,Pp,r'$P$',3,-2.5)
lab(ax,S,r'$S$',2.5,3.5,'sujet','l',weight='bold')
lab(ax,(O[0],B[1]),'tangente horizontale',4,-4,'fixe','s',ha='left') if False else None
text(ax,62,B[1]-9,r'$BS\approx 1{,}4281$','varie','s',ha='left')
text(ax,62,B[1]-15,r'$OS\approx 1{,}7434$','sujet','s',ha='left')
text(ax,28,B[1]+4,'tangente horizontale','fixe','s')
save(fig,'31-017')
