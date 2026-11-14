import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(62)
C=(30,32); R=24
ang=[90,210,330]
ring=lambda a:(C[0]+R*math.cos(math.radians(a)),C[1]+R*math.sin(math.radians(a)))
line(ax,arc(C,R,0,2*math.pi,120),'fixe')
for a in ang: line(ax,[C,ring(a)],'fixe')
for i,a in enumerate(ang):
    b=ang[(i+1)%3]+(360 if i==2 else 0)
    line(ax,arc(C,R*0.45,math.radians(a+12),math.radians(b-12)),'varie',lw=1.3)
    m=math.radians((a+b)/2); text(ax,C[0]+R*0.72*math.cos(m),C[1]+R*0.72*math.sin(m),r'$\frac{2\pi}{3}$','varie','s')
for a in ang: disc(ax,ring(a)[0],ring(a)[1],1.6,'sujet')
disc(ax,C[0],C[1],0.9,'fixe')
text(ax,72,50,'$n=3$ points','sujet','m')
text(ax,72,38,r'$\frac{2\pi}{n}=\frac{2\pi}{3}$','varie','m')
text(ax,72,28,'≈ 2,094 rad','varie','s'); text(ax,72,23,'= 120°','varie','s')
save(fig,'29-138')
