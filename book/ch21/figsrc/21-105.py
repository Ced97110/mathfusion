import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,'un tour = trois gestes','encre','s')
for i,g in enumerate(['diviser','multiplier','soustraire']):
    box(ax,4+i*28,48,25,8,'varie',label=g,size='s')
    if i<2: arrow(ax,(29.5+i*28,52),(31.5+i*28,52),'varie')
box(ax,4,22,24,18,'sujet'); text(ax,16,34,'tour 1','sujet','s'); text(ax,16,27,'reste 3','sujet','s')
box(ax,34,22,24,18,'sujet'); text(ax,46,34,'tour 2','sujet','s'); text(ax,46,27,'reste 0','sujet','s')
arrow(ax,(28.5,31),(33.5,31),'varie'); arrow(ax,(58.5,31),(63.5,31),'resultat')
box(ax,64,22,21,18,'resultat',label='arrêt',size='m')
text(ax,44,12,r'$156\div12$ : arrêt : le reste est 0','resultat','s')
save(fig,'21-105')
