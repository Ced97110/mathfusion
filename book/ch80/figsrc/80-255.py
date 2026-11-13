import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,69,'3 contrôles : un ordre','sujet','s')
for i,x in enumerate((6,34,62)):
    box(ax,x,48,20,10,'sujet',label=r'$\mu(%d,3)=%d$'%(i+1,(0,-1,1)[i]),size='s')
    if i<2: arrow(ax,(x+20.5,53),(x+27.5,53),'fixe')
    box(ax,x,18,20,10,'autre',label=r'$\mu(%d,3)=%d$'%(i+1,(0,0,1)[i]),size='s')
text(ax,44,36,'3 élèves : aucun ordre','autre','s')
text(ax,44,6,r'$\mu$ de $S$ : ces coefficients','resultat','s')
save(fig,'80-255')
