import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,34,20,10,'sujet',label=r'$\sqrt{5}+2$',size='m'); arrow(ax,(22,39),(36,39),'varie'); text(ax,29,45,'conjugué','varie','s')
box(ax,36,34,20,10,'varie',label=r'$\sqrt{5}-2$',size='m')
box(ax,60,34,26,10,'resultat',label=r'produit : $5-4=1$',size='s')
box(ax,2,10,20,10,'sujet',label=r'$\sqrt{5}+2$',size='m'); arrow(ax,(22,15),(36,15),'autre'); text(ax,29,21,'opposé','autre','s')
box(ax,36,10,20,10,'autre',label=r'$-\sqrt{5}-2$',size='m')
text(ax,46,28,'seul le signe du milieu change','varie','s'); text(ax,72,15,'tous les signes','autre','s'); text(ax,72,9,'changent','autre','s')
save(fig,'18-115')
