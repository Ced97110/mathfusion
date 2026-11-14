import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
P=[(15,45),(41,45),(41,19),(15,19)]
poly(ax,P,'fixe')
for k,(x,y) in enumerate(P):
    disc(ax,x,y,3.2,'sujet' if k==0 else 'fixe',label=str(k+1))
for k in range(4):
    (x0,y0),(x1,y1)=P[k],P[(k+1)%4]
    dx,dy=x1-x0,y1-y0; n=math.hypot(dx,dy); ux,uy=dx/n,dy/n
    arrow(ax,(x0+4.2*ux,y0+4.2*uy),(x1-4.2*ux,y1-4.2*uy),'varie',curve=-0.4)
for (x,y),s in zip([(48,50),(48,14),(8,14),(8,50)],[r'$r$',r'$r^2$',r'$r^3$',r'$r^4$']):
    text(ax,x,y,s,'varie','m')
text(ax,28,61,'trajet du coin 1','sujet','s')
box(ax,60,36,24,10,'resultat',label=r'$r^4=1$',size='l')
text(ax,72,29,'carré inchangé','resultat','s')
save(fig,'49-002')
