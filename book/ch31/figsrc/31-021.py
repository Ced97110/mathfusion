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
u=4.0
a=(6,12); b=(a[0]+10*CO*u,12); c=(b[0],12+10*SI*u)
poly(ax,[a,b,c],'sujet'); rmark(ax,b,(-1,0),(0,1))
line(ax,arcpts(a,8,0,35),'encre',lw=0.8); text(ax,a[0]+12,a[1]+2.5,r'$35^\circ$','encre','s')
text(ax,(a[0]+c[0])/2-4,(a[1]+c[1])/2+3,'10','sujet','m',weight='bold')
text(ax,b[0]+2,(b[1]+c[1])/2,'5,736','varie','m',ha='left',weight='bold')
a2=(55,12); k=0.5
b2=(a2[0]+CO*u*10*k,12); c2=(b2[0],12+SI*u*10*k)
poly(ax,[a2,b2,c2],'resultat'); rmark(ax,b2,(-1,0),(0,1),1.8)
line(ax,arcpts(a2,6,0,35),'encre',lw=0.8)
text(ax,(a2[0]+c2[0])/2-4,(a2[1]+c2[1])/2+2.5,'1','resultat','m',weight='bold')
text(ax,b2[0]+2,(b2[1]+c2[1])/2,'0,5736','resultat','s',ha='left')
text(ax,44,46,r'$5{,}736\div 10=0{,}5736$','encre','m')
text(ax,44,40,r'$\sin 35^\circ=0{,}5736$','resultat','m')
text(ax,24,4,'hypoténuse 10','sujet','s'); text(ax,66,4,'hypoténuse 1','resultat','s')
save(fig,'31-021')
