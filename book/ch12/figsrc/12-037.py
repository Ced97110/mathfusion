import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
text(ax,44,39,'strictement : pas d’égalité','sujet','m')
box(ax,6,12,34,16,'resultat',label=r'$8>5$',size='l'); text(ax,23,7,'vrai','resultat')
box(ax,48,12,34,16,'limite',label=r'$8>8$',size='l'); text(ax,65,7,'faux','limite')
save(fig,'12-037')
