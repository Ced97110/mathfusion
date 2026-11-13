import sys,math; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cy=44; r=22; cl=30; cr=58
h=math.sqrt(r*r-14*14)
a0=math.atan2(h,14)
lens=[]
for k in range(21):
    t=-a0+2*a0*k/20
    lens.append((cl+r*math.cos(t),cy+r*math.sin(t)))   # arc of left circle (right side)
for k in range(21):
    t=(math.pi-a0)+2*a0*k/20
    lens.append((cr+r*math.cos(t),cy+r*math.sin(t)))
poly(ax,lens,'resultat')
disc(ax,cl,cy,r,'sujet',fill=False,lw=1.1)
disc(ax,cr,cy,r,'autre',fill=False,lw=1.1)
text(ax,22,74,'diviseurs de 12','sujet','m'); text(ax,66,74,'diviseurs de 18','autre','m')
for y,v in [(50,'4'),(38,'12')]: text(ax,17,y,v,'sujet','l')
for y,v in [(50,'9'),(38,'18')]: text(ax,71,y,v,'autre','l')
for (x,y,v) in [(40,50,'1'),(48,50,'2'),(40,38,'3'),(48,38,'6')]: text(ax,x,y,v,'resultat','l',weight='bold')
text(ax,44,10,'dans les deux : diviseurs communs','resultat','s')
arrow(ax,(44,14),(44,25),'resultat')
save(fig,'05-070')
