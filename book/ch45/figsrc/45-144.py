import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
for y,l in zip([38,24,10],[r'horloge : $0$','rotations : rotation nulle',r'fractions, $\times$ : $1$']):
    box(ax,2,y,44,10,'fixe',label=l,size='s'); arrow(ax,(47,y+5),(61,28),'varie')
box(ax,62,18,24,20,'sujet',label=r'$0$',size='xl',weight='bold')
text(ax,74,12,r'$a+0=a$','sujet','s')
save(fig,'45-144')
