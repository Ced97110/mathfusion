import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,24,57,'la taille : change avec x','limite','s')
text(ax,67,57,'divisibilité : toujours','resultat','s')
k=4; x0=14
text(ax,6,47,'$x+1$','sujet','s'); text(ax,6,40,'$2x$','varie','s')
text(ax,26,52,'$x=3$','fixe','s')
for y,v,ro in [(44,4,'sujet'),(37,6,'varie')]:
    box(ax,x0,y-3,v*k,6,ro,r=0.3); text(ax,x0+v*k+3,y,str(v),ro,'s')
text(ax,26,29,'$x=0$','fixe','s')
box(ax,x0,19,1*k,6,'sujet',r=0.3); text(ax,x0+k+3,22,'1','sujet','s')
text(ax,x0+1.5,15,'0','varie','s')
text(ax,6,22,'$x+1$','sujet','s') if False else None
box(ax,50,35,34,12,'resultat',label='$x^2-1=(x+1)(x-1)$',size='s')
arrow(ax,(67,34),(67,25),'varie')
box(ax,50,12,34,12,'sujet',label='$x+1$ divise $x^2-1$',size='s')
save(fig,'05-111')
