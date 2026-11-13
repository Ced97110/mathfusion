import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$2x \equiv 4 \ (\mathrm{mod}\ 8)$','sujet','l')
box(ax,3,40,38,10,'varie',label=r'$x=2$ : $2\times2=4$')
box(ax,47,40,38,10,'varie',label=r'$x=6$ : $2\times6\equiv4$')
box(ax,29,12,30,10,'resultat',label=r'$4$')
arrow(ax,(22,40),(36,23),'varie'); arrow(ax,(66,40),(52,23),'varie')
text(ax,44,5,'deux solutions : plus d’unicité','limite','s')
save(fig,'44-241')
