import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,3,10,52,42,'sujet')
text(ax,29,46,'même heure que 3','sujet','s')
for i,v in enumerate(['…','−9','3','15','27','39','…']): text(ax,8+i*7.8,30,v,'sujet','s')
arrow(ax,(56,31),(63,31),'varie')
box(ax,64,18,21,26,'resultat',label=r'$\bar{3}$',size='xl')
text(ax,29,17,'un paquet infini','sujet','s')
text(ax,74.5,12,'un seul nom','resultat','s') if False else None
save(fig,'47-047')
