import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for x,d in zip([34,44,54],'123'): box(ax,x-5,50,10,9,'fixe',label=d,size='m')
text(ax,27,54.5,'départ','fixe','s',ha='right')
for x,d,r in [(14,'1','resultat'),(24,'2','resultat'),(34,'3','resultat'),(54,'3','limite'),(64,'1','limite'),(74,'2','limite')]:
    box(ax,x-5,22,10,9,r,label=d,size='m')
text(ax,24,40,r'$A\,A\,B\,B$','resultat','m'); text(ax,64,40,r'$A\,B\,A\,B$','limite','m')
arrow(ax,(40,49),(26,43),'varie'); arrow(ax,(48,49),(62,43),'varie')
text(ax,24,14,'remet tout en place','resultat','s'); text(ax,64,14,'ordre 3, 1, 2','limite','s')
save(fig,'45-135')
