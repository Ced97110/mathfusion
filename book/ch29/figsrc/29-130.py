import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(58)
E0=(8,32); r=60; h=math.asin(9/r)
tip=lambda s:(E0[0]+r*math.cos(s*h),E0[1]+r*math.sin(s*h))
disc(ax,E0[0],E0[1],1.3,'sujet'); text(ax,E0[0],E0[1]-5,'œil','sujet','s')
line(ax,[E0,tip(1)],'fixe'); line(ax,[E0,tip(-1)],'fixe')
line(ax,arc(E0,r,-h,h),'varie',lw=1.6)
disc(ax,tip(0)[0]+9,E0[1],9,'fixe'); text(ax,tip(0)[0]+9,E0[1],'Lune','fixe','s')
line(ax,[E0,tip(0)],'fixe',dash=True)
text(ax,56,E0[1]+3.3,r'$r$ = 384 400 km','fixe','s')
a=arc(E0,16,-h*1.0,h*1.0); line(ax,arc(E0,22,-h,h),'sujet',lw=1.2); text(ax,33,E0[1]+8,'','sujet','s')
text(ax,30,E0[1]+9.5,r'$\theta\approx 0{,}00908$ rad','sujet','s')
arrow(ax,(36,E0[1]+8),(26+8,E0[1]+3.5),'sujet') if False else None
text(ax,44,14,r'$s=r\theta\approx 3\,490$ km','varie','m')
text(ax,44,7,r'(0,52° $\times\ \pi/180$ = 0,00908 rad)','encre','s')
save(fig,'29-130')
