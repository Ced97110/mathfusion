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
A=P_(1,0); T=P_(1,TA); Pp=P_(CO,SI)
line(ax,[A,(A[0],A[1]+34)],'fixe',lw=1.0); line(ax,[(A[0],A[1]-3),A],'fixe',lw=1.0)
line(ax,[O,T],'fixe',lw=0.9); line(ax,[A,T],'resultat',lw=2.2)
dot(ax,A,'sujet',1.3); dot(ax,O); dot(ax,Pp); dot(ax,T,'resultat',1.1)
lab(ax,O,r'$O$',-3,-2.5); lab(ax,A,r'$A$',-3,-3); lab(ax,T,r'$T$',3,1.5); lab(ax,Pp,r'$P$',-2.5,2.5)
text(ax,A[0]+3,A[1]+35,'tangente en $A$','fixe','s',ha='left') if False else None
text(ax,62,45,'droite tangente en $A$','fixe','s',ha='left') if False else None
text(ax,A[0]+4,A[1]+30,'tangente','fixe','s',ha='left')
text(ax,A[0]+4,A[1]+25.5,'en $A$','fixe','s',ha='left')
text(ax,A[0]+5,A[1]+9,'$AT=0{,}7002$','resultat','s',ha='left')
text(ax,A[0]+5,A[1]+4.5,r'$=\tan 35^\circ$','resultat','s',ha='left')
save(fig,'31-028')
