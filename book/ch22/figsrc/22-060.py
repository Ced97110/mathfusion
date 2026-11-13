import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$y\neq 0$','fixe','m')
box(ax,2,42,40,11,role='sujet',label=r'$\sqrt{x/y}$'); text(ax,44,47.5,'=','encre','l'); box(ax,46,42,40,11,role='autre',label=r'$\sqrt{x}/\sqrt{y}$')
text(ax,44,37,r'$x=9$, $y=4$','fixe','s')
box(ax,2,22,40,12,role='resultat',label=r'$\sqrt{9/4}=1{,}5$'); text(ax,44,28,'=','encre','l'); box(ax,46,22,40,12,role='resultat',label=r'$\frac{3}{2}=1{,}5$')
box(ax,2,4,84,10,role='limite',label=r'$y=0$ : $9/0$ n’existe pas')
save(fig,'22-060')
