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
u=17.0
def tri(x0,role,w,h,names,nums):
    a=(x0,10); b=(x0+w,10); c=(x0+w,10+h)
    poly(ax,[a,b,c],role); rmark(ax,b,(-1,0),(0,1),1.8)
    text(ax,(a[0]+b[0])/2,a[1]-3,nums[0],role,'s'); text(ax,b[0]+1.5,(b[1]+c[1])/2,nums[1],role,'s',ha='left')
    text(ax,(a[0]+c[0])/2-3.5,(a[1]+c[1])/2+3,nums[2],role,'s')
    text(ax,x0+w/2,38,names,role,'m',weight='bold')
    return a
a=tri(3,'sujet',CO*u,SI*u,'OHP',('0,8192','0,5736','1'))
line(ax,arcpts(a,5,0,35),'encre',lw=0.8)
a=tri(29,'autre',u,TA*u,'OAT',('1','0,7002','1,2208'))
line(ax,arcpts(a,5,0,35),'encre',lw=0.8)
w3=1.4281*13.6; h3=13.6; x0=63
poly(ax,[(x0,10),(x0+w3,10),(x0+w3,10+h3)],'resultat') if False else None
# OBS: right angle at top-left, 35 at the right end
a=(x0,10); b=(x0+w3,10); c=(x0,10+h3)
poly(ax,[a,b,c],'resultat'); rmark(ax,a,(1,0),(0,1),1.8)
text(ax,(a[0]+b[0])/2,a[1]-3,'1,4281','resultat','s') if False else None
text(ax,x0-1.5,10+h3/2,'1','resultat','s',ha='right')
text(ax,x0+w3/2,10-3,'1,4281','resultat','s')
text(ax,x0+w3/2+3,10+h3/2-3,'1,7434','resultat','s')
line(ax,arcpts(b,5,180-35,180),'encre',lw=0.8)
text(ax,x0+w3/2,38,'OBS','resultat','m',weight='bold')
text(ax,44,3,r'angle de $35^\circ$ (arc noir) dans chaque triangle','encre','s')
save(fig,'31-020')
