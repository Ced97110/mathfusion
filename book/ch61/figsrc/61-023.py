import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,3,3,82,74,'sujet',fill=False,lw=1.3)
text(ax,44,70,r'plus petit corps contenant','sujet','m'); text(ax,44,64,r'$\mathbb{Q}$ et $\sqrt{2}$','sujet','m')
box(ax,8,40,24,16,'fixe',label=r'$\mathbb{Q}$',size='l'); text(ax,20,59,'au départ','fixe','s')
disc(ax,64,48,7,'varie',label=r'$\sqrt{2}$'); text(ax,64,59,'ajouté','varie','s')
xs=(8,33,60)
for x,lab,(sx,sy),op in zip(xs,(r'$3\sqrt{2}$',r'$1+\sqrt{2}$',r'$\frac{1}{1+\sqrt{2}}$'),((16,40),(30,40),(64,41)),(r'$\times$',r'$+$',r'$\div$')):
    box(ax,x,6,24,14,'resultat',label=lab,size='s')
    arrow(ax,(sx,sy),(x+12,21),'resultat')
    text(ax,(sx+x+12)/2+3,31,op,'resultat','m')
save(fig,'61-023')
