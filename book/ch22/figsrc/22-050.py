import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'on répondrait : $\sqrt{x^2}=x$','encre','m')
box(ax,2,26,16,12,role='sujet',label=r'$x$'); arrow(ax,(20,32),(32,32),'varie'); text(ax,26,36,'carré','varie','s')
box(ax,34,26,18,12,role='sujet',label=r'$x^2$'); arrow(ax,(54,32),(68,32),'varie'); text(ax,61,36,'racine','varie','s')
box(ax,70,26,16,12,role='encre',fill=False,dash=True,label=r'$x$ ?')
box(ax,6,4,76,12,role='resultat',label=r'pour $x=5$, ça marche',size='m')
save(fig,'22-050')
