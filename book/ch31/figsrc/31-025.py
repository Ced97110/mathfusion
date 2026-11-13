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
def tri(x0,L,angs,role,name):
    a1,a2,a3=[math.radians(v) for v in angs]
    b=(x0+L,10); apex=(x0+L*math.sin(a2)*math.cos(a1)/math.sin(a3), 10+L*math.sin(a2)*math.sin(a1)/math.sin(a3))
    a=(x0,10); poly(ax,[a,b,apex],role)
    text(ax,x0+L/2,5,name,role,'s')
    return a,b,apex
def lbl(p,s,dx,dy,role): text(ax,p[0]+dx,p[1]+dy,s,role,'s')
a,b,c=tri(3,16,(35,55,90)[0:1]+(90,55),'sujet','OHP')
# angles: 35 at left, 90 at right, 55 at apex
lbl(a,'35°',4.5,2,'sujet'); lbl(b,'90°',-1,3.5,'sujet'); lbl(c,'55°',-2,-5.5,'sujet') if False else lbl(c,'55°',5,1,'sujet')
a,b,c=tri(32,22,(35,90,55),'autre','OAT')
lbl(a,'35°',5,2,'autre'); lbl(b,'90°',-1,3.5,'autre'); lbl(c,'55°',5,1,'autre')
a,b,c=tri(62,22,(35,60,85),'limite','autre triangle')
lbl(a,'35°',5,2,'limite'); lbl(b,'60°',-4.5,2.8,'limite'); lbl(c,'85°',0,3,'limite')
save(fig,'31-025')
