import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,22,50,'barre : un couple','autre','s'); text(ax,64,50,'crochets : un nombre','sujet','s')
line(ax,[(42,8),(42,46)],'fixe',dash=True)
box(ax,4,26,36,14,'autre',label='$E/F$',size='l')
text(ax,22,20,'deux corps','autre','s'); text(ax,22,12,'pas de calcul','limite','s')
box(ax,44,26,40,14,'sujet',label='$[E:F]=4$',size='l')
text(ax,64,20,'un nombre','sujet','s'); text(ax,64,12,'$4 = 2 \\times 2$','resultat','m')
save(fig,'61-044')
