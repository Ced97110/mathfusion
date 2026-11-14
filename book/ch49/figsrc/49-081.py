import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
box(ax,24,88,40,8,'fixe',label='trois relations')
arrow(ax,(44,88),(44,80),'encre')
# step 1: 8 forms (heavy step)
box(ax,4,50,80,30,'varie',fill=False,lw=1.8)
text(ax,44,76,'① rangement des mots','varie','m',weight='bold')
xs=[8+i*9.4 for i in range(8)]
for i,x in enumerate(xs):
    box(ax,x,57,7.4,7.4,'sujet')
brace(ax,xs[0],xs[3]+7.4,56,'sujet',label=r'4 formes $x^k$')
brace(ax,xs[4],xs[7]+7.4,56,'sujet',label=r'4 formes $x^ky$')
text(ax,44,70.5,'au plus 8 éléments dans G′','varie','s')
arrow(ax,(44,50),(44,41),'encre')
# step 2
box(ax,4,28,80,11,'autre',label='② D₄ vérifie les relations')
arrow(ax,(44,28),(44,20),'encre')
box(ax,4,6,80,12,'resultat',label='③ 8 sur 8 : bijection')
save(fig,'49-081')
