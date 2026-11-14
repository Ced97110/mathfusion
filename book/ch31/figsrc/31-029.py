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
fig,ax=canvas(60)
O3=(40.0,30.0); R3=22.0
line(ax,arcpts(O3,R3,0,360,120),'fixe')
Pp=(O3[0]+R3*CO,O3[1]+R3*SI); Q=(O3[0]-R3*CO,O3[1]-R3*SI); T=(O3[0]+1.2208*R3*CO,O3[1]+1.2208*R3*SI)
line(ax,[(O3[0]-1.2*R3*CO,O3[1]-1.2*R3*SI),T],'sujet',lw=1.2)
line(ax,[O3,T],'resultat',lw=2.4)
for p in (Q,Pp): dot(ax,p,'sujet',1.2)
dot(ax,O3); dot(ax,T,'resultat',1.1)
lab(ax,O3,r'$O$',2.5,-3); lab(ax,Pp,r'$P$',-2.5,3.5); lab(ax,T,r'$T$',3,1.5)
text(ax,Q[0]+2,Q[1]-5,'elle entre','sujet','s')
text(ax,Pp[0]+10,Pp[1]-8,'elle sort','sujet','s')
text(ax,O3[0]+19,O3[1]-1,'$OT=1{,}2208$','resultat','s')
text(ax,16,52,'droite $OP$ : sécante','sujet','s',ha='left') if False else None
save(fig,'31-029')
