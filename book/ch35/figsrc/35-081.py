import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
y0=34;k=3.6;x0=8;x1=76
f=numberline(ax,x0,x1,y0,0,360,step=90,every=2,arrow_right=False)
g=lambda t:y0+k*5*math.sin(math.radians(t+53.13))
line(ax,[(f(t),g(t)) for t in range(0,361,3)],'sujet',lw=1.3)
yc=y0+3*k
line(ax,[(x0,yc),(x1,yc)],'varie',lw=1.1)
text(ax,83,yc,'$c=3$','varie','m')
for t,lab in ((90,'90°'),(343.74,'343,74°')):
    line(ax,[(f(t),yc),(f(t),y0-8)],'resultat',dash=True,lw=0.7)
    disc(ax,f(t),yc,1.3,'resultat')
    text(ax,f(t),y0-11,lab,'resultat','m')
text(ax,49,9,r'$3\sin x+4\cos x$','sujet','m')
text(ax,44,66,'deux solutions entre 0° et 360°','resultat','m')
save(fig,'35-081')
