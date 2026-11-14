import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,20,54,r'$1x$','sujet','l'); text(ax,68,54,r'$x$','sujet','l')
arrow(ax,(28,54),(60,54),'varie'); text(ax,44,49.5,"le 1 n’est pas écrit",'varie','s')
for i in range(5):
    box(ax,10+14*i,26,12,10,'sujet' if i==0 else 'autre',label=r'$x$')
brace(ax,10,22,26,'sujet',label=r'$1x$'); brace(ax,24,76,26,'autre',label=r'$4x$')
brace(ax,10,76,38,'resultat',label=r'$x+4x=5x$',down=False)
save(fig,'15-033')
