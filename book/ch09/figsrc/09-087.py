import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
for i in range(10): box(ax,9+7*i,36,7,10,'resultat' if i<3 else 'sujet',r=0.3)
brace(ax,9,30,46,'resultat',label=r'part $P$ = 15 €',down=False)
brace(ax,9,79,36,'sujet',label=r'base $B$ = 50 €')
text(ax,44,20,'le morceau que 30 % désigne','fixe','s')
save(fig,'09-087')
