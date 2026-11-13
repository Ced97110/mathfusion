import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,22,52,r'$x=1$','encre','m',weight='bold'); text(ax,66,52,r'$x=-2$','encre','m',weight='bold')
box(ax,4,34,36,12,'limite',label=r'$3\times4=12$',size='m'); box(ax,48,34,36,12,'resultat',label=r'$0\times1=0$',size='m')
text(ax,22,26,'aucun facteur nul','limite','s'); text(ax,66,26,r'$x+2$ est nul','resultat','m',weight='bold')
text(ax,22,15,'produit non nul','limite','m'); text(ax,66,15,'un facteur est nul','resultat','m')
text(ax,44,5,'produit nul : un facteur est nul','encre','s')
save(fig,'18-110')
