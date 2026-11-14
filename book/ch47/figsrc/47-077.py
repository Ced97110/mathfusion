import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for i in range(3):
    x=4+i*28
    box(ax,x,26,24,14,'sujet' if i==0 else 'fixe',r=0.5)
    for k in range(2): disc(ax,x+7+k*10,33,2.8,'sujet' if i==0 else 'fixe')
brace(ax,4,84,42,'fixe',label=r'$|G|=6$ éléments',down=False)
brace(ax,4,28,24,'sujet',label=r'$|H|=2$')
text(ax,70,13,r'$[G:H]=3$','varie','m')
text(ax,44,4,r'$2\times3=6$','resultat','l')
save(fig,'47-077')
