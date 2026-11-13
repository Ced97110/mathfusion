import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
box(ax,2,19,16,12,'sujet',label=r'$a=0$')
arrow(ax,(19,25),(25,25),'varie')
for i in range(2):
    for j in range(2): box(ax,26+j*9,16+i*9,9,9,'fixe',label='0',r=0.4)
text(ax,35,10,'matrice nulle','fixe','s')
labs=[r'trace $T(0)=0$',r'norme $N(0)=0$',r'$m(\lambda)=\lambda$']
for y,l in zip([35,20.5,6],labs):
    box(ax,54,y,32,9,'resultat',label=l,size='s')
    arrow(ax,(44,25),(54,y+4.5),'varie')
text(ax,70,3,'','fixe') if False else None
save(fig,'77-098')
