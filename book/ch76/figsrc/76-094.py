import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,37,44,14,12,'sujet',label=r'$F$',size='xl')
text(ax,44,60,'F est l’un de ces ensembles','sujet','s')
names=['réels','rationnels','complexes']
for i,n in enumerate(names):
    x=4+i*28
    box(ax,x,22,24,10,'autre',label=n,size='m')
    arrow(ax,(44,43),(x+12,33),'varie')
brace(ax,4,80,20,'resultat',r'$+$   $-$   $\times$   $\div$  (sauf par 0)',down=True,size='m')
save(fig,'76-094')
