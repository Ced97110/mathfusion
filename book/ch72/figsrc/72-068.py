import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$u$ de carré $B(u,u)=1$ et $x=(2,1)$','encre','s')
box(ax,3,30,39,20,'sujet'); box(ax,46,30,39,20,'autre')
text(ax,22,45,'avec B','sujet','m'); text(ax,22,38,r'$2\times1\,/\,1 = 2$','sujet','m')
text(ax,65,45,'avec Q(u) = 1/2','autre','m'); text(ax,65,38,r'$1\,/\,(1/2) = 2$','autre','m')
arrow(ax,(22,29),(38,17),'resultat'); arrow(ax,(65,29),(50,17),'resultat')
box(ax,24,5,40,12,'resultat',label=r'on retire 2 fois $u$')
save(fig,'72-068')
