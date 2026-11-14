import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y0=32;k=3.4;x0=6;x1=70
f=lambda u:x0+(u+90)/360*(x1-x0)
g=lambda u:y0+k*5*math.sin(math.radians(u))
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.6)
for yy,lab in ((y0+5*k,'sommet $R$'),(y0-5*k,'creux $-R$')):
    line(ax,[(x0,yy),(x1,yy)],'fixe',dash=True,lw=0.7); text(ax,79,yy,lab,'fixe','s')
line(ax,[(f(u),g(u)) for u in range(-90,91,3)],'sujet',lw=1.4)
line(ax,[(f(u),g(u)) for u in range(90,271,3)],'autre',lw=1.4)
yc=y0+3*k
line(ax,[(x0,yc),(x1,yc)],'varie',lw=1.1); text(ax,79,yc,'$c=3$','varie','s')
for u in (36.87,143.13): disc(ax,f(u),yc,1.2,'resultat')
text(ax,22,7,'montée : 1 solution','sujet','s')
text(ax,60,7,'descente : 1 solution','autre','s')
save(fig,'35-083')
