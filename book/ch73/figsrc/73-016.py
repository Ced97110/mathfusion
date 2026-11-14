import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
u=14; y0=18
poly(ax,[(4,y0),(4+u,y0),(4+u,y0+u),(4,y0+u)],'sujet')
poly(ax,[(30,y0),(30+u,y0),(30+1.5*u,y0+u),(30+0.5*u,y0+u)],'resultat')
line(ax,[(30+u,y0),(30+u,y0+u)],'resultat',dash=True)
poly(ax,[(58,y0),(58+2*u,y0),(58+2*u,y0+u),(58,y0+u)],'limite')
text(ax,44,42,'aire = base × hauteur','encre','m')
text(ax,11,y0+u+4,'carré','sujet','s'); text(ax,40.5,y0+u+4,'cisaillement','resultat','s'); text(ax,72,y0+u+4,'dilatation','limite','s')
text(ax,11,y0-4,'1 × 1 = 1','sujet','s'); text(ax,37,y0-4,'1 × 1 = 1','resultat','s'); text(ax,72,y0-4,'2 × 1 = 2','limite','s')
save(fig,'73-016')
