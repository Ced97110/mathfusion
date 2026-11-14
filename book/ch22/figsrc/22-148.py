import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,24,50,40,12,'sujet',label=r'$\sqrt{b^2-4ac}$')
arrow(ax,(34,50),(22,36),'varie'); arrow(ax,(54,50),(66,36),'varie')
text(ax,22,31,r'$a=1,\ b=2,\ c=-2$','fixe','s'); text(ax,66,31,r'$a=b=c=1$','fixe','s')
box(ax,2,10,40,18,'resultat',label=r'radicande 12'+'\n'+r'$\sqrt{12}=2\sqrt{3}$')
box(ax,46,10,40,18,'limite',label='radicande −3\npas de solution réelle')
save(fig,'22-148')
