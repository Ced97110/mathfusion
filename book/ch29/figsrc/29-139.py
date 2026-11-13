import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(58)
gy=22; a=11; x0=14; dist=2*a
line(ax,[(4,gy),(84,gy)],'fixe',lw=1.2)
cyc=[(x0+a*(t-math.sin(t)),gy+a*(1-math.cos(t))) for t in [i*2/60 for i in range(61)]]
line(ax,cyc,'varie',lw=1.3)
c1=(x0,gy+a); c2=(x0+a*2,gy+a)
line(ax,arc(c1,a,0,2*math.pi,100),'fixe'); line(ax,arc(c2,a,0,2*math.pi,100),'sujet',lw=1.1)
disc(ax,x0,gy,1.1,'varie'); v=cyc[-1]; disc(ax,v[0],v[1],1.1,'varie')
line(ax,[c2,(c2[0],gy)],'sujet'); line(ax,[c2,v],'sujet')
line(ax,arc(c2,5,-math.pi/2,-math.pi/2+2) if False else arc(c2,5,-math.pi/2,-math.pi/2-2),'sujet',lw=1.0)
text(ax,c2[0]+8,c2[1]-9,r'$t$ = 2 rad','sujet','s') if False else None
text(ax,c2[0]+3.5,c2[1]-3.5,r'$t$','sujet','s')
brace(ax,x0,x0+a*2,gy,'resultat',label=r'$at$ = 0,35 $\times$ 2 = 0,7 m',size='s')
text(ax,50,46,'cycloïde : trace de la valve','varie','s',ha='left')
text(ax,50,38,r'roue : $a$ = 0,35 m','sujet','s',ha='left')
text(ax,50,33.5,r'rotation : $t$ = 2 rad','sujet','s',ha='left')
text(ax,50,29,'distance au sol = arc','resultat','s',ha='left') if False else None
save(fig,'29-139')
