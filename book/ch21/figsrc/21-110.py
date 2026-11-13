import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,35,66,'juste','resultat','m'); text(ax,70,66,'faux','limite','m')
G=['1. diviser','2. multiplier','3. soustraire']
Y=[50,32,14]
for g,y in zip(G,Y):
    text(ax,11,y+5,g,'varie','s')
box(ax,22,Y[0],27,10,'resultat',label=r'$x^2\div x=x$',size='s')
box(ax,22,Y[1],27,10,'resultat',label=r'$x(x+2)=x^2+2x$',size='s')
box(ax,22,Y[2],27,10,'resultat',label=r'$-(x^2+2x)\to3x+6$',size='s')
box(ax,54,Y[0],32,10,'limite',label=r'$5x\div x=5$',size='s')
box(ax,54,Y[2],32,10,'limite',label=r'$-x^2+2x\to7x+6$',size='s')
text(ax,70,Y[0]-4,'un seul terme à la fois','limite','s')
text(ax,70,Y[2]-4,'oubli de la parenthèse','limite','s')
text(ax,35.5,Y[1]-3.5,'tout le diviseur','resultat','s')
text(ax,35.5,Y[2]-3.5,'tout le produit','resultat','s')
save(fig,'21-110')
