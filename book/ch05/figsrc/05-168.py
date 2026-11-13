import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(106)
xs=[14,30,46,62]
for x,l in zip(xs,['2','3','5','7']): box(ax,x,80,12,10,'sujet',label=l)
text(ax,20,96,r'$p_1$','sujet','m'); text(ax,68,96,r'$p_n$','sujet','m')
brace(ax,14,74,80,'sujet','multiplier tous')
arrow(ax,(44,72),(44,64),'varie')
box(ax,32,54,24,10,'varie',label='210')
arrow(ax,(44,54),(44,44),'varie'); text(ax,50,49,'plus 1','varie','s',ha='left')
box(ax,32,34,24,10,'resultat',label=r'$P=211$')
arrow(ax,(44,34),(44,24),'varie'); text(ax,50,29,'÷ 2, ÷ 3, ÷ 5, ÷ 7','varie','s',ha='left')
box(ax,16,12,56,11,'resultat',label='reste 1 à chaque fois')
save(fig,'05-168')
