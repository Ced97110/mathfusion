import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(48)
f=numberline(ax,6,74,14,0,14,step=1,every=2,arrow_right=True)
text(ax,44,43,r'$x=\frac{\pi}{6}+2k\pi$','sujet','l')
pts=[(math.pi/6,0,'0,524'),(math.pi/6+2*math.pi,1,'6,807'),(math.pi/6+4*math.pi,2,'13,09')]
for v,k,lab in pts:
    disc(ax,f(v),14,1.4,'sujet')
    text(ax,f(v),17.5,f'$k={k}$','sujet','s')
    text(ax,f(v),4.5,lab,'resultat','s')
for (a,_,_),(b,_,_) in zip(pts,pts[1:]):
    arrow(ax,(f(a)+1,21),(f(b)-1,21),'varie',curve=-0.45)
    text(ax,(f(a)+f(b))/2,29,r'$+2\pi$','varie','s')
save(fig,'29-135')
