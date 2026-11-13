import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[58+6*i for i in range(5)]
def row(y,label,green=False,red=False):
    text(ax,4,y,label,'encre','s',ha='left')
    box(ax,48,y-5,38,10,'sujet',fill=False,dash=True)
    for i,x in enumerate(xs): disc(ax,x,y,1.4,'resultat' if (green and i==0) else 'sujet')
row(52,'1. un ensemble non vide')
row(36,'2. son plus petit élément',green=True)
text(ax,xs[0],43.5,'r','resultat','s')
row(18,'3. si c’est faux, un élément',green=True)
text(ax,4,13.5,'encore plus petit existe','encre','s',ha='left')
disc(ax,52,18,1.4,'limite'); arrow(ax,(xs[0]-1.8,18),(53.8,18),'varie')
text(ax,52,11,r'$r-b$','limite','s'); text(ax,xs[0]+3,25,'r','resultat','s')
text(ax,66,4,'contradiction : on s’arrête','limite','s')
save(fig,'05-042')
