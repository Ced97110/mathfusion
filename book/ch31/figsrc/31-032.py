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
B=P_(0,1); Pp=P_(CO,SI)
line(ax,[O,P_(1.35*CO,1.35*SI)],'fixe',lw=1.0)
line(ax,arcpts(O,10,0,35),'sujet',lw=1.6); line(ax,arcpts(O,14,35,90),'resultat',lw=1.6)
line(ax,arcpts(O,20,0,90),'fixe',lw=0.5) if False else None
rmark(ax,O,(1,0),(0,1),5)
text(ax,O[0]+14,O[1]+3,r'$35^\circ$','sujet','s')
text(ax,O[0]+7.5,O[1]+19,r'$55^\circ$','resultat','s')
text(ax,62,32,r'$90^\circ$ entre les axes','fixe','s',ha='left')
text(ax,62,25,r'$90^\circ-35^\circ=55^\circ$','resultat','s',ha='left')
text(ax,62,18,'$\\theta=35^\\circ$','sujet','s',ha='left') if False else None
dot(ax,O); lab(ax,O,r'$O$',-3,-2.5)
save(fig,'31-032')
