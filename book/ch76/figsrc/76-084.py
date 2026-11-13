import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$G$','sujet','l')
box(ax,28,48,14,8,'sujet',label='1',size='l'); box(ax,46,48,14,8,'sujet',label=r'$s$',size='l')
arrow(ax,(44,46),(44,38),'varie')
box(ax,6,12,76,22,'resultat',fill=True)
xs=[10,26,40,55,64,78]
box(ax,10,17,10,12,'autre',label='3',size='l'); text(ax,24,23,r'$\times$','encre','m'); box(ax,28,17,10,12,'sujet',label='1',size='l')
text(ax,44,23,'+','encre','l'); box(ax,48,17,10,12,'autre',label='2',size='l'); text(ax,62,23,r'$\times$','encre','m'); box(ax,66,17,10,12,'sujet',label=r'$s$',size='l')
text(ax,15,8,'nombres de $F$','autre','s'); text(ax,70,8,'un élément de $F[G]$','resultat','s')
save(fig,'76-084')
