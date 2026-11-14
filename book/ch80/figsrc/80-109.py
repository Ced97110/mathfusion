import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,22,64,'conjuguer : bijective','resultat','s'); text(ax,66,64,'application nulle','limite','s')
box(ax,3,34,38,24,'resultat',label=None); box(ax,47,34,38,24,'limite',label=None)
text(ax,22,52,r'$(a,a)\mapsto(\bar a,\bar a)$','resultat','s'); text(ax,22,42,'deux fois : retour au départ','resultat','s')
text(ax,66,52,r'$U\neq W$ : deux droites','limite','s'); text(ax,66,42,r'$\eta(U)=\eta(W)=\{0\}$','limite','s')
box(ax,3,6,38,18,'resultat',label='inclusion gardée',size='s'); box(ax,47,6,38,18,'limite',label=r'$U\subseteq W$ faux',size='s')
arrow(ax,(22,34),(22,25),'resultat'); arrow(ax,(66,34),(66,25),'limite')
save(fig,'80-109')
