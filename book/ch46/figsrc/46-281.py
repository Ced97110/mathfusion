import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,59,'5 solutions de l’équation','sujet','m')
xs=[10+16*i for i in range(5)]
for i,x in enumerate(xs): box(ax,x-6,42,12,9,'sujet',label=f'$x_{i+1}$')
perm=[1,0,2,3,4]
for i,x in enumerate(xs):
    j=perm[i]; box(ax,xs[j]-6,18,12,9,'varie',label=f'$x_{i+1}$')
    arrow(ax,(x,41.5),(xs[j],27.5),'varie')
text(ax,44,34.5,'','encre')
text(ax,44,10,r'mélange = permutation : $S_{5}$','varie','s')
text(ax,44,4,r'paires : $A_{5}$','resultat','s')
save(fig,'46-281')
