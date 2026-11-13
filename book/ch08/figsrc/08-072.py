import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,6,57,r'$1 \div 3$','sujet','m',ha='left')
for k,s in enumerate(['0,3','0,33','0,333']):
    text(ax,10,47-k*8,s,'sujet','l',ha='left')
text(ax,10,23,r'0,333','sujet','l',ha='left')
text(ax,10+12.9,23,r'$\ldots$','varie','xl',ha='left')
text(ax,10,10,'la liste ne finit jamais','fixe','s',ha='left')
arrow(ax,(46,23),(52,23),'varie')
text(ax,54,27,'« et cela','varie','s',ha='left'); text(ax,54,19,'continue sans fin »','varie','s',ha='left')
save(fig,'08-072')
