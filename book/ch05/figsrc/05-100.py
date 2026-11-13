import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
k=76/1008; x0=6
text(ax,x0,52,r'$252\times 4=1\,008$','sujet','s',ha='left')
for i in range(4): box(ax,x0+i*252*k,38,252*k,9,'sujet',r=0.3)
text(ax,x0,32,r'$198\times 5=990$ : on retire 198, 5 fois','autre','s',ha='left')
for i in range(5): box(ax,x0+i*198*k,19,198*k,9,'autre',r=0.3)
xe=x0+990*k; xt=x0+1008*k
ax.add_patch(Rectangle((xe,38),xt-xe,9,fc=COL['resultat'],ec=COL['resultat'],lw=0.5,zorder=3))
arrow(ax,(xt-0.7,10),(xt-0.7,37),'resultat',curve=0)  if False else None
arrow(ax,(xt-0.7,51),(xt-0.7,48),'resultat'); text(ax,xt-2,53,'18','resultat','m',ha='center')
text(ax,6,10,r'$1\,008-990=18$','resultat','m',ha='left')
text(ax,70,10,r'$v=-5$','autre','m')
save(fig,'05-100')
