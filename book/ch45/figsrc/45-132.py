import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
u=12; x0=8
spec={2:('sujet','2 quarts'),1:('varie','1 quart'),3:('autre','3 quarts')}
for y,order in [(34,[2,1,3]),(10,[3,2,1])]:
    x=x0
    for v in order:
        role,l=spec[v]; box(ax,x,y,v*u,12,role,label=l,size='s'); x+=v*u
brace(ax,x0,x0+6*u,48,'resultat',label='6 quarts',down=False)
brace(ax,x0,x0+6*u,9,'resultat',label='6 quarts',down=True)
arrow(ax,(44,33),(44,23),'varie'); text(ax,48,28,'autre ordre','varie','s',ha='left')
save(fig,'45-132')
