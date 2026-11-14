import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,6,12,26,30,'sujet',dash=True); box(ax,56,12,26,30,'resultat',dash=True)
ys={0:32,3:20}
for v,y in ys.items(): disc(ax,19,y,4,'sujet',label=str(v))
for v,y in {2:32,5:20}.items(): disc(ax,69,y,4,'resultat',label=str(v))
arrow(ax,(23.5,32),(64.5,32),'varie'); arrow(ax,(23.5,20),(64.5,20),'varie')
text(ax,44,36,'+ 2','varie','m')
text(ax,19,46,'H','sujet','l'); text(ax,69,46,'aH','resultat','l')
text(ax,44,6,'aL : chaque x devient a + x','varie','s')
save(fig,'45-248')
