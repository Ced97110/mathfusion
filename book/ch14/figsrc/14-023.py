import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,78,r'$2^3 \times 2^2 = 2^5 = 32$','resultat','l')
for i in range(5): box(ax,5.5+16*i,60,13,10,'sujet',label='2')
brace(ax,5.5,82.5,60,'resultat',label='5 facteurs égaux')
text(ax,44,36,r'$2^3 \times 3^2 = 72$','limite','l')
for i in range(5): box(ax,5.5+16*i,18,13,10,'sujet' if i<3 else 'autre',label='2' if i<3 else '3')
brace(ax,5.5,82.5,18,'limite',label='5 facteurs, pas égaux')
save(fig,'14-023')
