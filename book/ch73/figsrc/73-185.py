import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
P=[(17,46),(8,28),(26,28)]
for i,j in [(0,1),(1,2),(0,2)]: line(ax,[P[i],P[j]],'fixe')
for k,(x,y) in enumerate(P): disc(ax,x,y,3.6,'fixe',label=str(k+1))
text(ax,17,18,r'$S_3$ : 6 façons','sujet','s')
rows=[('tout couple → tout couple','✓','resultat'),(r'$G=G^{\prime}$','✗','limite'),('conjugués de l’échange : $S_3$','✓','resultat')]
for k,(l,m,r) in enumerate(rows):
    y=48-13*k; box(ax,36,y,38,9,r,label=l,size='s'); text(ax,81,y+4.5,m,r,'xl',weight='bold')
text(ax,55,16,'2 conditions vraies, 1 fausse','encre','s')
text(ax,55,9,r'$S_3$ contient $A_3$ normal : pas simple','encre','s')
[p.set_zorder(3.5) for p in ax.patches if isinstance(p,Circle)]
save(fig,'73-185')
