import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'idéal engendré par 6 et 10','sujet','m')
box(ax,10,42,22,10,'sujet',label='6'); box(ax,56,42,22,10,'sujet',label='10')
arrow(ax,(21,42),(38,33),'varie'); arrow(ax,(67,42),(50,33),'varie')
box(ax,24,24,40,9,'varie',label=r'$2\times6-10=2$',size='s')
arrow(ax,(44,24),(44,17),'resultat')
box(ax,14,8,60,9,'resultat',label=r'$(6,10)=(2)$ : multiples de 2',size='s')
save(fig,'52-287')
