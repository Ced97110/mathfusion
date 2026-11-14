import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(40)
box(ax,4,18,20,12,'sujet',label=r'$\sqrt{75}$'); box(ax,34,18,20,12,'varie',label=r'$\sqrt{25\times3}$'); box(ax,64,18,20,12,'resultat',label=r'$5\sqrt{3}$')
arrow(ax,(24.5,24),(33.5,24),'encre'); arrow(ax,(54.5,24),(63.5,24),'encre')
text(ax,29,12,'75 = 25 × 3','varie','s'); text(ax,59,12,r'$\sqrt{25}=5$','varie','s')
save(fig,'22-150')
