import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,3,3,82,70,'fixe',dash=True); text(ax,10,67,r'$R$','fixe','l')
box(ax,9,9,70,48,'autre'); text(ax,44,52,'tout sous-anneau S contient 1','autre','s')
box(ax,17,14,54,28,'sujet',label=None)
text(ax,44,34,'les multiples de 1','sujet','s')
text(ax,44,22,r'$0,\ 1,\ 1+1,\ 1+1+1,\ \ldots$','sujet','s')
save(fig,'52-201')
