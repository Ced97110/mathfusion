import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(60)
ox,oy=8,30; sx=sy=10.5
f=lambda x,y:(ox+x*sx,oy+y*sy)
arrow(ax,(ox-2,oy),(ox+2*math.pi*sx+8,oy),'fixe',lw=0.8); arrow(ax,(ox,oy-14),(ox,oy+16),'fixe',lw=0.8)
xs=[i*2*math.pi/160 for i in range(161)]
line(ax,[f(x,math.sin(x)) for x in xs],'sujet',lw=1.3)
line(ax,[f(0,0),f(1.45,1.45)],'varie',lw=1.1)
for v,l in [(math.pi,r'$\pi$'),(2*math.pi,r'$2\pi$')]:
    ax.plot([f(v,0)[0]]*2,[oy-1,oy+1],color=COL['fixe'],lw=0.8); text(ax,f(v,0)[0],oy-3.5,l,'fixe','s')
ax.plot([ox-1,ox+1],[f(0,1)[1]]*2,color=COL['fixe'],lw=0.8); text(ax,ox-3,f(0,1)[1],'1','fixe','s')
ax.plot([f(1,0)[0]]*2,[oy-1,oy+1],color=COL['fixe'],lw=0.8); text(ax,f(1,0)[0],oy-3.5,'1','fixe','s')
text(ax,f(2.0,0)[0]+10,oy+13,r'$y=\sin x$','sujet','m')
text(ax,f(1.45,1.45)[0]+9,f(1.45,1.45)[1]+2,r'$y=x$','varie','m')
text(ax,38,55,'mêmes échelles sur les deux axes','fixe','s')
text(ax,24,6,'près de 0 : collées','resultat','s') if False else None
text(ax,26,10,'près de 0 : courbe collée à la droite','resultat','s')
save(fig,'29-133')
