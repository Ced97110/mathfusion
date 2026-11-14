import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(50)
G=(8,22); D=66; h=0.11
T0=(G[0]+D,G[1]); T1=(G[0]+D*math.cos(h),G[1]+D*math.sin(h))
line(ax,[G,T0],'fixe'); line(ax,[G,T1],'varie')
line(ax,arc(G,D,0,h),'varie',lw=2.4)
disc(ax,G[0],G[1],1.4,'sujet'); text(ax,G[0]+1,G[1]-5,'géomètre','sujet','s')
disc(ax,T0[0],T0[1],1.1,'fixe'); disc(ax,T1[0],T1[1],1.1,'varie')
text(ax,T0[0]+2,T0[1]-4,'point visé','fixe','s',ha='center')
line(ax,arc(G,18,0,h),'sujet',lw=1.1)
text(ax,28,G[1]+7,r'erreur $\theta$ = 0,001 rad','sujet','s')
brace(ax,G[0],T0[0],G[1]-9,'fixe',label=r'$r$ = 100 m',down=True)
text(ax,70,G[1]+13.5,r'$s$ = 0,1 m','varie','s')
text(ax,44,45,r'$s=r\theta=100\times 0{,}001=0{,}1$ m','varie','m') if False else None
text(ax,44,45,r'$s=r\theta=100\times 0{,}001$ = 0,1 m','varie','s')
save(fig,'29-137')
