import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for i in range(5): box(ax,15+12*i,40,10,10,'varie' if i<3 else 'autre',label='2')
brace(ax,15,49,50,'varie',label='$n$ = 3',down=False)
brace(ax,51,73,50,'autre',label='$m$ = 2',down=False)
brace(ax,15,73,40,'resultat',label='$n+m$ = 5 facteurs')
arrow(ax,(44,33),(44,20),'resultat')
box(ax,30,8,28,11,'resultat',label=r'$2^{n+m}$',size='l')
save(fig,'14-027')
