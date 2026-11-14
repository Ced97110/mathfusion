import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,24,64,'base 2','sujet','m',weight='bold'); text(ax,64,64,r'base $e$','autre','m',weight='bold')
for y,a,b in [(50,r'$2^0=1$',r'$e^0=1$'),(36,r'$2^1=2$',r'$e^1\approx 2{,}718$'),(22,r'$2^{x+y}=2^x\,2^y$',r'$e^{x+y}=e^x\,e^y$')]:
    box(ax,3,y-5,40,10,'sujet',label=a,size='s')
    box(ax,46,y-5,39,10,'autre',label=b,size='s')
ax.add_patch(Rectangle((2,15),84,14,fc='none',ec=COL['resultat'],lw=1.2,ls='--',zorder=3))
text(ax,44,9,'même forme de règle','resultat','s')
save(fig,'45-040')
