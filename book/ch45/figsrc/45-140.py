import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,2,4,84,56,'fixe',fill=False,r=2); text(ax,14,55,'groupe','fixe','s')
box(ax,36,10,16,36,'resultat',r=1)
box(ax,8,10,44,36,'sujet',fill=False,lw=1.1,r=2); box(ax,36,10,44,36,'autre',fill=False,lw=1.1,r=2)
text(ax,21,40,r'$C(a)$','sujet','m'); text(ax,67,40,r'$C(b)$','autre','m'); text(ax,44,40,'centre','resultat','s',weight='bold')
disc(ax,44,28,3.5,'resultat',label=r'$e$'); text(ax,44,19,'neutre','resultat','s')
text(ax,62,55,r'dans tous les $C(a)$','encre','s')
save(fig,'45-140')
