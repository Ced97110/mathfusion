import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
rs=['sujet','varie','resultat','autre']
text(ax,44,57,r'$\mathbb{Z}$ : les entiers de 0 à 11','encre','m')
for n in range(12): box(ax,4+7*n,38,7,8,rs[n%4],label=str(n),size='s',r=0.4)
for k in range(4):
    x=4+k*21
    box(ax,x,10,19,12,rs[k],label=f'{{{k}, {k+4}, {k+8}…}}',size='s')
    arrow(ax,(x+9.5,36),(x+9.5,23.5),rs[k])
text(ax,44,4,r'$\mathbb{Z}/4\mathbb{Z}$ : 4 paquets. De même FG/K','encre','s')
text(ax,44,30,'on identifie si la différence est dans 4ℤ','encre','s')
save(fig,'49-066')
