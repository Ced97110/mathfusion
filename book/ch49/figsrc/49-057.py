import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
for i in range(4):
    for j in range(4):
        if (i,j) not in ((1,0),(0,1)): disc(ax,20+9*i,10+9*j,0.9,'fixe')
disc(ax,29,10,2,'sujet'); disc(ax,20,19,2,'autre')
text(ax,29,5.5,'(1, 0)','sujet','s'); text(ax,17,19,'(0, 1)','autre','s',ha='right')
text(ax,33.5,42,r'$\mathbb{Z}^2$','fixe','l')
text(ax,56,32,r'$x_1\mapsto(1,0)$','sujet','m',ha='left'); text(ax,56,24,r'$x_2\mapsto(0,1)$','autre','m',ha='left')
text(ax,71,14,'images différentes','resultat','s'); text(ax,71,9,r'donc $\bar{x}_1\neq\bar{x}_2$','resultat','s')
save(fig,'49-057')
