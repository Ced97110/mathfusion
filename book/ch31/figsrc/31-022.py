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
R2=40.0; O2=(8.0,10.0)
a=O2; b=(O2[0]+CO*R2,10); c=(b[0],10+SI*R2)
poly(ax,[a,b,c],'sujet'); rmark(ax,b,(-1,0),(0,1))
for p in (a,b,c): dot(ax,p)
lab(ax,a,r'$O$',-3,-2.5); lab(ax,b,r'$H$',0,-3.5); lab(ax,c,r'$P$',2.5,2)
text(ax,(a[0]+b[0])/2,b[1]-8,'0,8192','sujet','m')
text(ax,b[0]+2,(b[1]+c[1])/2,'0,5736','varie','m',ha='left')
text(ax,(a[0]+c[0])/2-4,(a[1]+c[1])/2+4,'1','resultat','m')
text(ax,54,38,r'$0{,}8192^2\approx 0{,}6710$','sujet','s',ha='left')
text(ax,54,32,r'$0{,}5736^2\approx 0{,}3290$','varie','s',ha='left')
text(ax,54,26,r'$0{,}6710+0{,}3290=1$','resultat','s',ha='left')
text(ax,54,46,'angle droit en $H$','encre','s',ha='left')
save(fig,'31-022')
