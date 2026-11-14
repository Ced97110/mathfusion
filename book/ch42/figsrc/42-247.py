import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
y=58
box(ax,4,y-5,18,10,'fixe',label='8'); box(ax,66,y-5,18,10,'resultat',label='2')
arrow(ax,(23.5,y),(64.5,y),'sujet'); text(ax,44,y+4.5,r'$f^{-1}$','sujet','m')
text(ax,44,y-11,r'$f^{-1}(8)=2$','resultat','l')
text(ax,44,34,'≠','encre','xl',weight='bold')
y=18
box(ax,4,y-5,18,10,'fixe',label='8'); box(ax,35,y-5,18,10,'fixe',label='512'); box(ax,66,y-5,18,10,'limite',label=r'$1/512$',size='s')
arrow(ax,(23.5,y),(33.5,y),'varie'); arrow(ax,(54.5,y),(64.5,y),'varie')
text(ax,28.5,y+4.5,r'$f$','varie','m'); text(ax,59.5,y+4.5,'1 ÷','varie','s')
text(ax,44,y-11,r'$1/f(8)=1/512$','limite','m')
save(fig,'42-247')
