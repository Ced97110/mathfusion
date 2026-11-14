import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
ys=[80,56,32,8]
box(ax,4,ys[0],52,12,'fixe',label=r'$\langle Ax,Ay\rangle=(Ax)^t(Ay)$',size='s')
box(ax,4,ys[1],52,12,'fixe',label=r'$=x^tA^tAy$',size='s')
box(ax,4,ys[2],52,12,'varie',label=r'$=x^tIy$',size='s')
box(ax,4,ys[3],52,12,'resultat',label=r'$=x^ty=\langle x,y\rangle$',size='s')
for i in range(3):
    arrow(ax,(30,ys[i]),(30,ys[i+1]+12),'fixe' if i<1 else 'varie')
text(ax,34,ys[0]-6,'règle de la transposée','fixe','s',ha='left')
text(ax,34,ys[1]-6,r'remplacer $A^tA$','varie','s',ha='left')
box(ax,62,ys[2],22,12,'sujet',label=r'$A^tA=I$',size='s')
arrow(ax,(62,ys[2]+6),(57,ys[2]+6),'sujet')
text(ax,73,ys[2]+17,'étape clé','varie','s')
text(ax,73,ys[2]-4,'départ : propriété 2','sujet','s')
text(ax,70,ys[3]+6,'arrivée : propriété 3\n$x=(3,4),\\ y=(5,0)$ :\n$\\langle x,y\\rangle=15$','resultat','s')
save(fig,'73-226')
