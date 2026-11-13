import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,46,'de 12 : 1, 2, 3, 4, 6, 12','sujet','m')
text(ax,44,36,'de 18 : 1, 2, 3, 6, 9, 18','autre','m')
text(ax,44,26,'écrits dans les deux listes','resultat','s')
for i,v in enumerate(['1','2','3','6']):
    box(ax,10+i*18,10,14,12,'resultat',label=v,size='l',lw=(1.8 if v=='6' else 0.8))
arrow(ax,(71,9),(71,5.5),'varie')
text(ax,70,2.5,'le plus grand : 6','varie','m',weight='bold')
save(fig,'05-071')
