import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,54,r'$x\geq 0$ et $y\geq 0$','fixe','s')
box(ax,4,38,36,11,role='sujet',label=r'$\sqrt{xy}$'); text(ax,44,43.5,'=','encre','l'); box(ax,48,38,36,11,role='autre',label=r'$\sqrt{x}\,\sqrt{y}$')
arrow(ax,(22,38),(22,29),'varie'); arrow(ax,(66,38),(66,29),'varie'); text(ax,44,33.5,r'$x=9$, $y=4$','fixe','s')
box(ax,4,18,36,11,role='sujet',label=r'$\sqrt{36}=6$'); box(ax,48,18,36,11,role='autre',label=r'$3\times 2=6$')
text(ax,44,7,r'les deux ont pour carré $xy$','resultat','m')
save(fig,'22-059')
