import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,8,42,30,12,'limite',label=r'$\dim U=1$'); box(ax,48,42,30,12,'autre',label=r'$\dim U^{\perp}=1$')
text(ax,43,48,'+','encre','l')
arrow(ax,(43,40),(43,32),'varie'); text(ax,60,36,'1 + 1','varie','m')
box(ax,14,18,60,12,'resultat',label=r'$n=2$',size='l')
text(ax,44,11,'V : le plan entier','fixe','s')
text(ax,44,58,'la somme des dimensions vaut n','resultat','s')
save(fig,'72-107')
