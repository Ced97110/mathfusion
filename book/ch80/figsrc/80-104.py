import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,29,44,30,14,'sujet',label=r'$\eta$',size='xl')
text(ax,44,62,'une application sur les vecteurs','sujet','s')
box(ax,3,10,38,22,'sujet',label=None); box(ax,47,10,38,22,'autre',label=None)
text(ax,22,27,'1. somme','sujet','s'); text(ax,22,18,r'$\eta(x+y)=\eta(x)+\eta(y)$','sujet','s')
text(ax,66,27,'2. scalaire','autre','s'); text(ax,66,18,r'$\eta(ax)=\sigma(a)\eta(x)$','autre','s')
arrow(ax,(36,44),(22,33),'sujet'); arrow(ax,(52,44),(66,33),'autre')
save(fig,'80-104')
