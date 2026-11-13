import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,4,38,26,11,'sujet',label='50 miles',size='m'); text(ax,44,43.5,r'$\div$','encre','xl')
box(ax,58,38,26,11,'limite',label='0 gallon',size='m',dash=True)
text(ax,44,28,r'$? \times 0 = 50$','limite','l')
text(ax,44,19,'or tout nombre × 0 donne 0','fixe','s')
box(ax,14,3,60,10,'limite',label='aucun nombre : pas de taux',size='m')
save(fig,'09-107')
