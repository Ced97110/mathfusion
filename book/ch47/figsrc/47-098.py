import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,16,51,'départ','encre','m'); text(ax,48,51,'on regroupe','varie','m'); text(ax,75,51,'arrivée','encre','m')
box(ax,2,26,28,11,'sujet',label='26 − 2 = 24'); box(ax,2,10,28,11,'autre',label='27 − 3 = 24')
box(ax,36,18,24,12,'varie',label='24 + 24',size='l')
arrow(ax,(31,31.5),(36,26),'varie'); arrow(ax,(31,15.5),(36,22),'varie')
box(ax,65,18,21,12,'resultat',label='= 48',size='l'); arrow(ax,(61,24),(65,24),'varie')
text(ax,75.5,13,'= 4 × 12','resultat','m')
save(fig,'47-098')
