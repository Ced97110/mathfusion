import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,14,62,60,10,'sujet',label=r'$(x+2)(x+3)=0$')
arrow(ax,(44,61),(44,50),'varie'); text(ax,46,55.5,r'si $x+2$ vaut 5','varie','s',ha='left')
box(ax,14,38,60,10,'autre',label=r'$5\times(x+3)=0$')
arrow(ax,(44,37),(44,26),'varie'); text(ax,46,31.5,r'on divise 0 par 5','varie','s',ha='left')
box(ax,14,14,60,10,'resultat',label=r'$x+3=0$')
text(ax,44,6,'un facteur vaut zéro','resultat','s')
save(fig,'18-010')
