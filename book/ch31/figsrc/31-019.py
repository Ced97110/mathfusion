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
fig,ax=canvas(48)
quarter(ax)
Pp=P_(CO,SI); H=P_(CO,0)
line(ax,[O,H],'sujet',lw=1.8); line(ax,[H,Pp],'varie',lw=1.8); line(ax,[O,Pp],'fixe',lw=0.9)
rmark(ax,H,(-1,0),(0,1))
for p in (O,H,Pp): dot(ax,p)
lab(ax,O,r'$O$',-3,-2.5); lab(ax,H,r'$H$',0,-3.5); lab(ax,Pp,r'$P$',3,2)
text(ax,(O[0]+H[0])/2,O[1]-8,r'$OH=\cos\theta=0{,}8192$','sujet','s')
text(ax,H[0]+3,(H[1]+Pp[1])/2+2,r'$HP=\sin\theta$','varie','s',ha='left')
text(ax,H[0]+3,(H[1]+Pp[1])/2-2.5,r'$=0{,}5736$','varie','s',ha='left')
line(ax,arcpts(O,8,0,35),'fixe',lw=0.8); text(ax,O[0]+12,O[1]+2.8,r'$\theta$','fixe','s')
save(fig,'31-019')
