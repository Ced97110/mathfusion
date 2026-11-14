import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(64)
text(ax,44,34,r'$\sqrt[3]{2}$','sujet',40)
text(ax,20,56,'le 3 : un cube','varie','m'); text(ax,68,56,'le 2 : le nombre','varie','m')
arrow(ax,(26,52),(34,43),'varie'); arrow(ax,(62,52),(56,43),'varie')
text(ax,44,17,'le nombre positif dont','resultat','m'); text(ax,44,12,'le cube vaut 2','resultat','m')
text(ax,44,5.5,'≈ 1,2599 (jamais exact)','fixe','s')
save(fig,'61-007')
