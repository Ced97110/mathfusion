import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
xs=[18,44,70]
text(ax,2,79,r'$(H+N)/N$ : 3 éléments','sujet','s',ha='left'); text(ax,86,79,'cyclique','sujet','s',ha='right',weight='bold')
text(ax,2,41,r'$H/(H\cap N)$ : 3 éléments','autre','s',ha='left'); text(ax,86,41,'cyclique','autre','s',ha='right',weight='bold')
for x,l in zip(xs,[r'$\{0,6\}$',r'$\{4,10\}$',r'$\{8,2\}$']):
    box(ax,x-11,60,22,11,'sujet',label=l,size='m')
for x,l in zip(xs,['0','4','8']):
    box(ax,x-11,22,22,11,'autre',label=l,size='m')
    arrow(ax,(x,60),(x,33.6),'resultat',lw=1.4)
box(ax,4,3,80,12,'resultat',label='3 et 3, cycliques : isomorphes',size='s',weight='bold')
save(fig,'48-159')
