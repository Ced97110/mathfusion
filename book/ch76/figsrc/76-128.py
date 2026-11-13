import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def cell(x,y,r,l): box(ax,x,y,10,10,r,label=l)
for (x,y,r,l) in [(8,38,'fixe','$1$'),(18,38,'varie','$2$'),(8,28,'varie','$3$'),(18,28,'fixe','$4$'),
                  (56,38,'fixe','$1$'),(66,38,'varie','$3$'),(56,28,'varie','$2$'),(66,28,'fixe','$4$')]: cell(x,y,r,l)
arrow(ax,(32,43),(52,43),'varie',curve=-0.3); text(ax,42,52,'transposée','varie','m')
text(ax,19,53,r'$A$','sujet','m'); text(ax,67,53,r'$A^t$','sujet','m')
text(ax,19,18,r'$\det A=-2$','sujet','m'); text(ax,67,18,r'$\det A^t=-2$','sujet','m')
text(ax,43,18,'=','resultat','xl')
save(fig,'76-128')
