import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(66)
E0=(6,44); r=66; h=0.22
P=lambda s:(E0[0]+r*math.cos(s*h),E0[1]+r*math.sin(s*h))
line(ax,[E0,P(1)],'fixe'); line(ax,[E0,P(-1)],'fixe')
line(ax,arc(E0,r,-h,h),'varie',lw=1.8)
line(ax,[P(-1),P(1)],'sujet',lw=1.0)
disc(ax,E0[0],E0[1],1.3,'fixe'); text(ax,E0[0]+1,E0[1]-5,'œil','fixe','s')
text(ax,70,E0[1]+r*h+4.5,'arc et corde','encre','s') if False else None
text(ax,46,E0[1]+17,r'arc centré sur l’œil, rayon $r$','varie','s') if False else None
text(ax,40,E0[1]-6,'corde presque confondue avec l’arc','encre','s') if False else None
ytop=26
L=40
line(ax,[(8,ytop),(8+L,ytop)],'varie',lw=2.4); text(ax,52,ytop,r'arc $s=r\theta$','varie','s',ha='left')
line(ax,[(8,ytop-8),(8+L,ytop-8)],'sujet',lw=2.4); text(ax,52,ytop-8,r'corde $2r\sin\frac{\theta}{2}$','sujet','s',ha='left')
text(ax,44,ytop-17,'même longueur : ≈ 3 490 km','resultat','m')
text(ax,60,E0[1]+9,'corde','sujet','s'); text(ax,76,E0[1]-14,'arc','varie','s')
save(fig,'29-131')
