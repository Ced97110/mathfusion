import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,3,26,34,32,'autre'); box(ax,51,26,34,32,'sujet')
text(ax,20,62,r'$gH$ (à gauche)','autre','s'); text(ax,68,62,r'$Hg$ (à droite)','sujet','s')
text(ax,20,49,r'$r$','autre','m'); text(ax,20,37,r'$rs$','autre','m')
text(ax,68,49,r'$r$','sujet','m'); text(ax,68,37,r'$sr$','sujet','m')
text(ax,44,43,'≠','limite','xl')
text(ax,68,19,r'$sr=r^{3}s$','sujet','m')
text(ax,20,19,r'$g=r$, $H=\{1,s\}$','fixe','s')
arrow(ax,(68,34),(68,22.5),'fixe',lw=0.6) if False else None
save(fig,'47-040')
