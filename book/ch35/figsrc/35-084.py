import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y0=26;k=3.6;x0=6;x1=70
f=lambda u:x0+(u+90)/360*(x1-x0)
g=lambda u:y0+k*5*math.sin(math.radians(u))
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.6)
line(ax,[(f(u),g(u)) for u in range(-90,271,3)],'sujet',lw=1.4)
yc=y0+5*k
line(ax,[(x0,yc),(x1,yc)],'resultat',lw=1.2); text(ax,79,yc,'$c=R=5$','resultat','s')
disc(ax,f(90),yc,1.4,'encre')
line(ax,[(f(90),yc),(f(90),y0)],'fixe',dash=True,lw=0.7)
text(ax,f(90),y0-3.5,'90°','fixe','s')
text(ax,38,52,'la droite touche le sommet','resultat','m')
text(ax,38,8,'53,13° + 36,87° = 90°','resultat','s')
save(fig,'35-084')
