import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'« 4 fois un nombre »','encre','m')
for i in range(4): box(ax,6+i*19,36,16,12,'sujet',label='$x$',size='l')
brace(ax,6,79,35,'sujet',label='$4x$ = 4 fois $x$',down=True)
text(ax,44,16,r'$x=5$ : $4\times5=20$','resultat','m')
text(ax,44,8,'produit · fois · multiplié par','varie','s')
save(fig,'16-093')
