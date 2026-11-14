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
fig,ax=canvas(50)
u=48.0; x0=8
box(ax,x0,34,SI*u,7,'sujet'); box(ax,x0,20,TA*u,7,'resultat')
text(ax,x0+SI*u/2,37.5,'$HP=0{,}5736$','sujet','s'); text(ax,x0+TA*u/2,23.5,'$AT=0{,}7002$','resultat','s')
arrow(ax,(x0+SI*u+3,37.5),(x0+TA*u+4,26),'varie',curve=-0.3)
text(ax,62,31,r'$\times\,1{,}2208$','varie','s')
text(ax,44,11,r'$0{,}5736\div 0{,}8192=0{,}7002$','resultat','s')
text(ax,44,4,r'$\sin\theta\div\cos\theta=\tan\theta$','encre','s')
save(fig,'31-027')
