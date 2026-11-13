import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(52)
ox,oy=6,24; s=9.2; sy=12
f=lambda x,y:(ox+x*s,oy+y*sy)
arrow(ax,(ox-2,oy),(ox+7.9*s+5,oy),'fixe',lw=0.8)
tp=2*math.pi
xa=[i*tp/120 for i in range(121)]
xb=[tp+i*1.5/30 for i in range(31)]
line(ax,[f(x,math.sin(x)) for x in xa],'sujet',lw=1.5)
line(ax,[f(x,math.sin(x)) for x in xb],'fixe',lw=1.2)
for x0,lab in [(0,'0'),(tp,r'$2\pi$')]:
    ax.plot([f(x0,0)[0]]*2,[oy-1.2,oy+1.2],color=COL['fixe'],lw=0.8); text(ax,f(x0,0)[0],oy-4,lab,'fixe','s')
v=math.sin(0.5)
line(ax,[f(0.5,v),f(tp+0.5,v)],'varie',dash=True)
for x in (0.5,tp+0.5): disc(ax,f(x,v)[0],f(x,v)[1],1.1,'varie')
text(ax,f(0.5,0)[0]+1,oy+v*sy+8,r'$x=0{,}5$','varie','s')
text(ax,f(tp+0.5,0)[0],oy+v*sy+8,r'$x=0{,}5+2\pi$','varie','s')
text(ax,f(3.1,0)[0],oy-12,r'même sinus : $\sin$ = 0,479','varie','s') if False else None
brace(ax,f(0,0)[0],f(tp,0)[0],oy-6,'sujet',label='une période : de 0 à $2\\pi$',size='s')
text(ax,f(2.2,0)[0],oy+13.5,r'même valeur du sinus : 0,479','varie','s') if False else None
text(ax,f(0.9,0)[0]+1,oy-12,'','varie','s') if False else None
text(ax,34,47,'même valeur du sinus : 0,479','varie','m')
save(fig,'29-134')
