import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,12,62,r'$\mathbb{Z}$','sujet','l'); text(ax,70,62,'horloge 12 h','autre','m')
rows=[(46,'2','10'),(30,'3','3'),(14,'2+3=5','1')]
for y,a,b in rows:
    box(ax,3,y-5,24,10,'sujet',label=a)
    box(ax,56,y-5,28,10,'autre',label=b)
    arrow(ax,(27,y),(56,y),'varie')
text(ax,41.5,50.5,r'$\times 5$','varie','s'); text(ax,41.5,34.5,r'$\times 5$','varie','s'); text(ax,41.5,18.5,r'$\times 5$','varie','s')
text(ax,70,5,'10 + 3 = 1 : concorde','resultat','s')
save(fig,'46-278')
