import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,4,46,24,10,'sujet',label=r'$\mathbb{Z}$'); box(ax,4,26,24,10,'sujet',label=r'$(3)$'); box(ax,4,6,24,10,'sujet',label=r'$(6)$')
arrow(ax,(16,36),(16,46),'resultat'); arrow(ax,(16,16),(16,26),'limite')
text(ax,33,41,'aucun idéal entre : maximal','resultat','s',ha='left')
text(ax,33,21,r'$(3)$ est entre $(6)$ et $\mathbb{Z}$','limite','s',ha='left')
text(ax,33,31,'3 premier','sujet','s',ha='left'); text(ax,33,11,'6 composé','sujet','s',ha='left')
save(fig,'52-282')
