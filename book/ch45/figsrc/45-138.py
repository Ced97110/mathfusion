import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
xs=[3,24,45,66]
for x,l,r in zip(xs,['identité','échange','tout → 1','tout → 2'],['sujet','sujet','limite','limite']): box(ax,x,24,18,14,r,label=l,size='s')
box(ax,1,20,86,20,'resultat',fill=False,dash=True,r=2)
text(ax,44,45,r'$C(\mathrm{id})$ contient les 4','resultat','m')
brace(ax,3,42,19,'sujet',label='un inverse',down=True); brace(ax,45,84,19,'limite',label="pas d'inverse",down=True)
text(ax,44,6,'donc pas un sous-groupe','limite','m',weight='bold')
save(fig,'45-138')
