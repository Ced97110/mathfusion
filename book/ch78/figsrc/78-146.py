import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
vals=[1,1,0,0,0,0,0,0]
for i,v in enumerate(vals):
    box(ax,4+i*10,46,9,9,'sujet' if v else 'fixe',label=str(v))
text(ax,44,59,r'carrés des 8 coordonnées de $x$','encre','s')
brace(ax,4,84,46,'sujet',label=r'$Q(x)=2>0$',down=True)
arrow(ax,(44,36),(44,28),'varie'); text(ax,60,32,'on peut diviser','varie','s')
box(ax,6,12,76,14,'resultat',label=r'$x\cdot\bar{x}/Q(x)=1$')
text(ax,44,5,r'donc $x^{-1}$ existe si $x\neq 0$','resultat','m')
save(fig,'78-146')
