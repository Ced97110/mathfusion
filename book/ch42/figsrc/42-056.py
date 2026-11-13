import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
xs=[32,44,56,68]
text(ax,3,36,'ce livre : ℕ','sujet','s',ha='left')
text(ax,3,18,'Judson : ℕ','autre','s',ha='left')
for x,l in zip(xs,'0123'): disc(ax,x,36,4,'sujet',label=l,size='l')
text(ax,79,36,'…','sujet','xl')
ax.add_patch(Circle((32,18),4,ec=COL['varie'],fc='none',lw=0.9,ls='--',zorder=2)); text(ax,32,18,'0','varie','l')
for x,l in zip(xs[1:],'123'): disc(ax,x,18,4,'autre',label=l,size='l')
text(ax,79,18,'…','autre','xl')
arrow(ax,(32,31.5),(32,22.5),'varie',both=True)
text(ax,36,27,'seule différence','varie','s',ha='left')
save(fig,'42-056')
