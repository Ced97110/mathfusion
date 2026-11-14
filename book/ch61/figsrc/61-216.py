import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
cx=30
box(ax,cx-14,4,28,10,'sujet',label=r'$F_0 = \mathbb{Q}$')
box(ax,cx-19,22,38,10,'sujet',label=r'$F_1 = F_0(\sqrt{a_1})$',size='s')
arrow(ax,(cx,14),(cx,22),'varie')
text(ax,cx+3,18,r'ajoute $\sqrt{a_1}$','varie','s',ha='left')
text(ax,66,18,r'$a_1 \in F_0$','encre','s')
arrow(ax,(cx,32),(cx,36),'varie'); text(ax,cx,39.5,'⋮','fixe','l'); arrow(ax,(cx,43),(cx,47),'varie')
box(ax,cx-24,47,48,10,'sujet',label=r'$F_k$')
arrow(ax,(cx,57),(cx,63),'resultat')
box(ax,cx-14,63,28,10,'resultat',label=r'$a \in F_k$')
save(fig,'61-216')
