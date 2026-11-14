import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,22,60,'linéaire','fixe','m'); text(ax,66,60,'semi-linéaire','sujet','m')
box(ax,3,34,38,20,'fixe',label=None); box(ax,47,34,38,20,'sujet',label=None)
text(ax,22,47,r'$\eta(ax)=a\,\eta(x)$','fixe'); text(ax,66,47,r'$\eta(ax)=\sigma(a)\,\eta(x)$','sujet','s')
text(ax,22,39,r'$a=i$ : reste $i$','varie','s'); text(ax,66,39,r'$a=i$ : devient $-i$','varie','s')
box(ax,3,8,38,12,'fixe',label=r'$i\,\eta(x)$'); box(ax,47,8,38,12,'sujet',label=r'$-i\,\eta(x)$')
arrow(ax,(22,34),(22,21),'fixe'); arrow(ax,(66,34),(66,21),'sujet')
save(fig,'80-100')
