import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,22,32,12,'sujet',label=r'$6x+9$'); text(ax,18,38,'aire (somme)','sujet','s')
box(ax,52,22,34,12,'resultat',label=r'$3(2x+3)$'); text(ax,69,38,'côtés (produit)','resultat','s')
arrow(ax,(35,31),(51,31),'varie',lw=1.4); text(ax,43,35,'factoriser','varie','s')
arrow(ax,(51,25),(35,25),'fixe'); text(ax,43,20,'développer','fixe','s')
text(ax,44,8,'retrouver les dimensions','varie','s')
save(fig,'18-008')
