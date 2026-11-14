import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
box(ax,16.5,38,18,10,'sujet',label=r'$2^3$',size='l')
text(ax,37,44,'la puissance','sujet','s',ha='left')
for i in range(3):
    box(ax,6+15*i,16,9,9,'sujet',label='2')
for i in range(2):
    text(ax,18+15*i,20.5,r'$\times$','encre','m')
brace(ax,6,45,16,'sujet',label='3 facteurs 2')
arrow(ax,(25.5,38),(25.5,26.5),'varie')
box(ax,62,16,14,9,'resultat',label='8')
arrow(ax,(47,20.5),(61,20.5),'varie')
arrow(ax,(34.5,40),(69,27.5),'varie',curve=-0.2)
text(ax,69,12.3,'le résultat','resultat','s')
save(fig,'14-017')
