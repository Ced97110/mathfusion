import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,24,68,40,10,'sujet',label=r'produit $7\times8$')
for X,m,a,b,c in ((2,3,1,2,2),(31,4,3,0,0),(60,5,2,3,1)):
    box(ax,X,40,26,16,'autre',label=f'mod {m}\n{a} × {b} = {c}')
    arrow(ax,(44,68),(X+13,56.5),'sujet')
brace(ax,2,86,38,'autre',label='3 calculs en même temps',down=True)
arrow(ax,(44,28),(44,19.5),'resultat')
box(ax,14,6,60,12,'resultat',label='restes 2, 0, 1 → résultat',size='s')
save(fig,'52-239')
