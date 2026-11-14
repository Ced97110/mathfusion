import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'combien d’éléments ?','sujet','m')
rows=[(7,'limite','7 : règles qui imposent trop',44),(8,'resultat','8 : exact',30),(9,'limite','9 : règles qui disent peu',16)]
for n,r,l,y in rows:
    text(ax,2,y,l,r,'s',ha='left')
    for k in range(n): disc(ax,52+k*4,y,1.7,r)
save(fig,'49-007')
