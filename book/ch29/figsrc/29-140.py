import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(62)
C=(30,32); R=24
V=[(C[0]+R*math.cos(math.radians(90+72*k)),C[1]+R*math.sin(math.radians(90+72*k))) for k in range(5)]
line(ax,arc(C,R,0,2*math.pi,120),'fixe')
poly(ax,V,'sujet')
line(ax,[C,V[0]],'fixe'); line(ax,[C,V[1]],'fixe')
for v in V: disc(ax,v[0],v[1],1.3,'sujet')
line(ax,arc(C,9,math.radians(90),math.radians(162)),'varie',lw=1.4)
text(ax,C[0]-3.5,C[1]+13,r'$\frac{2\pi}{5}$','varie','s')
text(ax,70,50,'$n=5$ côtés','sujet','m')
text(ax,70,38,'angle au centre','varie','s')
text(ax,70,32,r'$\frac{2\pi}{5}$','varie','m')
text(ax,70,24,'≈ 1,257 rad','varie','s'); text(ax,70,19.5,'= 72°','varie','s')
save(fig,'29-140')
