import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
box(ax,3,44,82,28,'sujet'); text(ax,16,67,r'$\mathbb{Q}(s)$','sujet','m')
box(ax,7,47,36,12,'sujet',label=r'$s=\sqrt{2}+\sqrt{3}$',size='s')
box(ax,47,47,36,12,'sujet',label=r'$1/s=\sqrt{3}-\sqrt{2}$',size='s')
text(ax,14,41,'≈ 3,15','sujet','s'); text(ax,54,41,'≈ 0,32','sujet','s')
[arrow(ax,a,b,'varie') for a,b in [((25,44),(14,29)),((25,44),(60,29)),((65,44),(30,29)),((65,44),(72,29))]]
box(ax,3,17,38,12,'resultat',label=r'$s+1/s=2\sqrt{3}$',size='s')
box(ax,47,17,38,12,'resultat',label=r'$s-1/s=2\sqrt{2}$',size='s')
text(ax,44,6,r'$\sqrt{2}$ et $\sqrt{3}$ sont dans $\mathbb{Q}(s)$','resultat','m')
save(fig,'61-222')
