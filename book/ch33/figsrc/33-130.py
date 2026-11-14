import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(66)
cy=30; fx=lambda x: 45+math.copysign(math.log10(1+abs(x)),x)/3*33
fy=lambda x: cy+math.atan(x)/(math.pi/2)*22
line(ax,[(10,cy),(82,cy)],'fixe')
for s in (1,-1): line(ax,[(10,cy+s*22),(82,cy+s*22)],'fixe',dash=True)
for s,t in ((1,'90°'),(-1,'−90°')): text(ax,5,cy+s*22,t,'fixe','s')
xs=[10**(3*i/100)-1 for i in range(101)]
line(ax,[(fx(-x),fy(-x)) for x in xs[::-1]]+[(fx(x),fy(x)) for x in xs],'resultat',1.5)
for s,role in ((1,'fixe'),(-1,'sujet')):
    disc(ax,fx(1000*s),fy(1000*s),1.2,role if s<0 else 'sujet')
text(ax,72,cy+17,'89,94°','sujet','s'); text(ax,18,cy-17,'−89,94°','sujet','s')
text(ax,76,cy+3.5,'1 000','fixe','s'); text(ax,14,cy+3.5,'−1 000','fixe','s')
text(ax,45,6,'pente','fixe','s')
save(fig,'33-130')
