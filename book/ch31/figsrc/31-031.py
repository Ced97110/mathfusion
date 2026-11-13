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
poly(ax,[O,B,S],'resultat'); rmark(ax,B,(1,0),(0,-1))
for p in (O,B,S): dot(ax,p)
lab(ax,O,r'$O$',-3,-2.5); lab(ax,B,r'$B$',-3,3); lab(ax,S,r'$S$',2.5,3)
line(ax,arcpts(O,7,35,90),'encre',lw=0.8); text(ax,O[0]+4.5,O[1]+10,'$55^\\circ$','encre','s') if False else None
text(ax,O[0]+6,O[1]+12,r'$55^\circ$','encre','s')
text(ax,B[0]+14,B[1]+4,'1,4281','resultat','s') if False else None
text(ax,(B[0]+S[0])/2,B[1]+4,'1,4281','resultat','s')
text(ax,O[0]-3.5,(O[1]+B[1])/2,'1','resultat','s',ha='right') if False else None
text(ax,O[0]+3,(O[1]+B[1])/2+5,'1','resultat','s')
text(ax,(O[0]+S[0])/2+8,(O[1]+S[1])/2-4.5,'1,7434','resultat','s')
text(ax,32,47,'angle droit en $B$','encre','s')
save(fig,'31-031')
