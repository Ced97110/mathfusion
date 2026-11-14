import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,2,6,36,52,'sujet'); text(ax,20,53,'paquet « 1 chiffre »','sujet','s')
box(ax,7,34,26,10,'varie',label='3 × 3'); box(ax,7,14,26,10,'varie',label='4 × 5')
box(ax,54,38,32,10,'resultat',label='9 : un chiffre'); box(ax,54,12,32,10,'limite',label='20 : deux chiffres')
arrow(ax,(34,39),(53,43),'varie'); arrow(ax,(34,19),(53,17),'varie')
text(ax,70,30,'deux réponses','limite','m'); text(ax,70,26,'pas de produit','limite','m')
save(fig,'47-104')
