import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,6,44,32,14,'fixe',label=r'$\sqrt{-1}$',size='l'); box(ax,50,44,32,14,'sujet',label=r'$i$',size='xl',weight='bold')
arrow(ax,(39,51),(49,51),'varie'); text(ax,44,56,'même','varie','s'); text(ax,44,46,'nombre','varie','s')
text(ax,44,34,r'$i\times i=-1$','resultat','l')
box(ax,6,12,32,12,'fixe',label=r'$\mathbb{Z}[\sqrt{-1}]$',size='m'); box(ax,50,12,32,12,'sujet',label=r'$\mathbb{Z}[i]$',size='m')
arrow(ax,(39,18),(49,18),'varie',both=True); text(ax,44,27,'même ensemble','varie','s')
text(ax,44,5,r'$m+n\,i$,  $m$, $n$ entiers','sujet','s')
save(fig,'51-072')
