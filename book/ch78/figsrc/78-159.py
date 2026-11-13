import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
x0,y0=14,56
arrow(ax,(6,y0),(84,y0),'fixe'); arrow(ax,(x0,40),(x0,90),'fixe')
sx,sy=13,0.9
pts=[(x0+t*18,y0+(t**3-8)*1.8) for t in [i*0.05 for i in range(0,70)]]
pts=[(x,y) for x,y in pts if 40<=y<=90]
line(ax,pts,'sujet',lw=1.3)
disc(ax,x0+2*18,y0,1.8,'resultat')
text(ax,x0+2*18+10,y0-5,r'$\lambda=2$','resultat','m')
text(ax,x0+18,87,r'$t^3-8$','sujet','m')
text(ax,34,49.5,'part de $-\\infty$','fixe','s')
text(ax,50,86,'arrive à $+\\infty$','fixe','s')
text(ax,44,32,'traverse l’axe : racine réelle','resultat','s')
arrow(ax,(44,28),(44,22),'varie')
box(ax,4,6,80,14,'limite',label=r'$(a-\lambda 1)x=0$, $x\neq 0$',size='m')
save(fig,'78-159')
