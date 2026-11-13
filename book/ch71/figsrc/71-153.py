import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,59,r'corps $\{0,1\}$ : $1+1=0$','encre','m')
text(ax,26,53,'matrice de $B$','encre','s')
box(ax,6,34,13,12,'fixe',label='0'); box(ax,20,34,13,12,'sujet',label='1')
box(ax,6,20,13,12,'sujet',label='1'); box(ax,20,20,13,12,'fixe',label='0')
text(ax,63,53,'vecteurs non nuls','encre','s')
for y,u in zip((42,31,20),('(1,0)','(0,1)','(1,1)')):
    box(ax,42,y-4.5,42,9,'limite',label=r'$u=%s$ : $B(u,u)=0$'%u)
box(ax,6,3,76,10,'limite',label='diagonale nulle : impossible')
save(fig,'71-153')
