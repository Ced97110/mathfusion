import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,3,3,82,64,'varie')
text(ax,44,61,r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$ : on ajoute $\sqrt{3}$','varie','s')
box(ax,12,9,64,44,'sujet')
text(ax,44,47,r'$\mathbb{Q}(\sqrt{2})$ : on ajoute $\sqrt{2}$','sujet','s')
box(ax,22,14,44,24,'fixe',label=r'$\mathbb{Q}$ : les fractions',size='s')
save(fig,'61-020')
