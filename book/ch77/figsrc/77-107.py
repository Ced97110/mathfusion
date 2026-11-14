import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,2,36,12,12,'fixe',label=r'$u$')
text(ax,33,79,'en une fois','autre')
for i in range(4):
    for j in range(4): box(ax,24+j*4.5,55+i*4.5,4.5,4.5,'autre',r=0.3)
text(ax,33,51,r'$4\times4$','autre')
text(ax,43,37,'étage par étage','sujet')
for k,x in enumerate([22,48]):
    for i in range(2):
        for j in range(2): box(ax,x+j*8,14+i*8,8,8,'sujet',r=0.3)
    text(ax,x+8,9,r'$2\times2$','sujet')
box(ax,70,36,16,12,'resultat',label=r'$-8$')
arrow(ax,(14,44),(24,64),'varie'); arrow(ax,(14,40),(22,22),'varie')
arrow(ax,(42,64),(70,46),'varie'); arrow(ax,(38,22),(48,22),'varie'); arrow(ax,(64,22),(70,38),'varie')
save(fig,'77-107')
