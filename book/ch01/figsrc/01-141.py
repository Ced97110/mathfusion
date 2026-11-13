import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
C=[10,24,38,52,66,80]
for i,c in enumerate(C):
    box(ax,c-5,20,10,10,'limite' if i<3 else 'resultat',label=str(i))
for a,b in zip(C[:-1],C[1:]): arrow(ax,(a,30.5),(b,30.5),'varie',curve=-0.5)
brace(ax,5,85,39,'varie',label='passage : correct partout',down=False)
brace(ax,5,43,17,'limite',label='faux : 1 > 4, 2 > 5, 4 > 6')
brace(ax,47,85,17,'resultat',label='vrai : 8 > 7, …')
text(ax,44,5,'le départ bloque avant 3','limite','m')
save(fig,'01-141')
