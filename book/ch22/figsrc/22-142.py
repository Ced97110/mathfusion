import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
xs=[2,31,60]
box(ax,xs[0],22,26,14,'sujet',label='étapes 1 à 3\nm = −11')
box(ax,xs[1],22,26,14,'varie',label='étape 4\n2(−11)+3 = −19')
box(ax,xs[2],22,26,14,'limite',label='rejeté')
arrow(ax,(28.5,29),(30.5,29),'encre'); arrow(ax,(57.5,29),(59.5,29),'encre')
text(ax,15,15,'le calcul propose','sujet','s'); text(ax,44,15,'la vérification tranche','varie','s')
save(fig,'22-142')
