import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,10,56,40,10,'sujet'); box(ax,10,56,12,10,'resultat',label='15')
brace(ax,10,50,66,'sujet',label=r'base $B$ = 50',down=False)
text(ax,30,52,'30 % de 50','fixe','s')
box(ax,10,24,64,10,'sujet'); box(ax,10,24,12.8,10,'resultat',label='16')
brace(ax,10,74,34,'sujet',label=r'base $B$ = 80',down=False)
text(ax,42,20,'20 % de 80','fixe','s')
save(fig,'09-085')
