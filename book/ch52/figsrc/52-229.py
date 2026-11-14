import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,22.5,63,'inverse de 5','sujet','s',weight='bold')
text(ax,65.5,63,'8 : aucun inverse','autre','s',weight='bold')
Ls=[(46,'sujet',r'$5\times5=25$'),(30,'sujet',r'$25=2\times12+1$'),(10,'resultat','reste 1 : inverse')]
Rs=[(46,'autre',r'$8\times3=24$'),(30,'autre',r'$24=2\times12+0$'),(10,'limite','reste 0 : pas 1')]
for X,S,col in ((2,Ls,'sujet'),(45,Rs,'autre')):
    for i,(y,r,l) in enumerate(S):
        h=12 if i<2 else 14
        box(ax,X,y,41,h,r,label=l,size='s')
        if i: arrow(ax,(X+20.5,S[i-1][0]),(X+20.5,y+h+0.5),S[i-1][1] if i<2 else r)
save(fig,'52-229')
