import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,60,r'$x^2+x+1$ dans $\mathbb{Z}/2\mathbb{Z}$','sujet','m')
for i,(xv,calc) in enumerate([('0',r'$0+0+1=1$'),('1',r'$1+1+1=1$')]):
    x=3+i*43
    box(ax,x,22,39,28,'fixe')
    text(ax,x+19.5,44,rf'$x={xv}$','fixe','m'); text(ax,x+19.5,35,calc,'encre','s')
    box(ax,x+6,25,27,7,'limite',label=r'$\neq 0$',size='s')
text(ax,44,14,r'dans $\mathbb{Z}/2\mathbb{Z}$, $1+1=0$','varie','s')
text(ax,44,6,'2 essais sur 2 : aucune racine','limite','s')
save(fig,'61-139')
