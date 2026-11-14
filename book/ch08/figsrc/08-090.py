import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
c=0.7; x0=9
text(ax,x0,43,'1/3 = 100/300','sujet','m',ha='left')
for k in range(100): ax.add_patch(Rectangle((x0+k*c,32),c,6,ec=COL['sujet'],fc=FILL['sujet'],lw=0.25,zorder=2))
text(ax,x0,21,'0,33 = 99/300','autre','m',ha='left')
for k in range(100):
    if k<99: ax.add_patch(Rectangle((x0+k*c,10),c,6,ec=COL['autre'],fc=FILL['autre'],lw=0.25,zorder=2))
    else: ax.add_patch(Rectangle((x0+k*c,10),c,6,ec=COL['limite'],fc=FILL['limite'],lw=0.8,zorder=3))
arrow(ax,(x0+99.5*c,5.5),(x0+99.5*c,9),'limite')
text(ax,x0+99.5*c,2.5,'écart 1/300','limite','s',ha='right')
save(fig,'08-090')
