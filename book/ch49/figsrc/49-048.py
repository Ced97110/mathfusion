import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,4,32,36,12,'fixe',label=r'$x_i\,x_i^{-1}\,x_i$')
box(ax,56,32,28,12,'fixe',label=r'$x_i$')
text(ax,22,48,'mot de 3 lettres','fixe','s'); text(ax,70,48,'mot d’une lettre','fixe','s')
box(ax,28,8,32,14,'sujet',label=r'$\bar{x}_i$',size='l')
arrow(ax,(22,32),(38,23)); arrow(ax,(70,32),(50,23))
text(ax,44,3.5,'même classe : un seul élément','sujet','s')
save(fig,'49-048')
