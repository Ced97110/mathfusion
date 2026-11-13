import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
X=[18,44,70]
text(ax,44,63,r'un seul ensemble $S$','sujet','m',weight='bold')
text(ax,4,50,'départ','fixe','s',ha='left'); text(ax,4,14,'arrivée','fixe','s',ha='left')
for x,l in zip(X,['1','2','3']):
    disc(ax,x,50,4,'sujet',label=l); disc(ax,x,14,4,'sujet',label=l)
arrow(ax,(X[0]+1.5,45.5),(X[1]-1.5,18.5),'varie'); arrow(ax,(X[1]+1.5,45.5),(X[2]-1.5,18.5),'varie')
arrow(ax,(X[2]-1.5,45.5),(X[0]+1.5,18.5),'varie')
text(ax,44,4,r'$\pi$ : chaque place reçue une fois','varie','s')
save(fig,'42-248')
