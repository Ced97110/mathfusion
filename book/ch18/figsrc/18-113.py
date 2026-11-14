import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,46,r'valeurs de $x^2+1$','sujet','m',weight='bold')
f=numberline(ax,6,76,20,0,10,step=1,every=1,size='s')
for v,t in ((1,r'$x=0$'),(5,r'$x=2$'),(10,r'$x=-3$')):
    disc(ax,f(v),20,1.6,'sujet'); text(ax,f(v),30 if v!=1 else 27,t,'sujet','s')
ax.plot([f(0)-1.8,f(0)+1.8],[20-1.8,20+1.8],color=COL['limite'],lw=1.3,zorder=4)
ax.plot([f(0)-1.8,f(0)+1.8],[20+1.8,20-1.8],color=COL['limite'],lw=1.3,zorder=4)
text(ax,26,7,'aucune valeur ne donne 0','limite','m')
save(fig,'18-113')
