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
fig,ax=canvas(56)
quarter(ax)
Pp=P_(CO,SI); A=P_(1,0); T=P_(1,TA); B=P_(0,1); S=P_(1/TA,1); H=P_(CO,0)
line(ax,[A,(A[0],B[1])],'fixe',lw=0.5); line(ax,[B,(S[0]+3,B[1])],'fixe',lw=0.5)
line(ax,[O,H],'sujet',lw=2.0); line(ax,[H,Pp],'varie',lw=2.0)
line(ax,[A,T],'autre',lw=2.0); line(ax,[O,T],'resultat',lw=1.2)
line(ax,[B,S],'fixe',lw=2.0); line(ax,[O,S],'encre',lw=0.9,dash=True)
text(ax,H[0]-8,O[1]-3,'cos 0,8192','sujet','s')
text(ax,H[0]-1,H[1]+5,'sin 0,5736','varie','s',ha='right')
text(ax,A[0]+2,A[1]+3,'tan 0,7002','autre','s',ha='left')
text(ax,A[0]+3,T[1]+4,'sec 1,2208','resultat','s',ha='left')
text(ax,B[0]+8,B[1]+3,'cotan 1,4281','fixe','s',ha='left')
text(ax,S[0]+3,S[1]-4,'cosec 1,7434','encre','s',ha='left')
save(fig,'31-018')
