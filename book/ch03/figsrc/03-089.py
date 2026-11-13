import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,13,67,'6 532','encre','l')
for x,l in zip([26,40,54,68],'6532'):
    box(ax,x,62,12,10,'sujet',label=l,size='l')
for x,l in zip([26,40,54],['6×999','5×99','3×9']):
    box(ax,x,42,9,10,'fixe',label=l,size='s')
    line(ax,[(x+4.5,62),(x+4.5,52)],'fixe',lw=0.6)
text(ax,13,47,'multiples de 3','fixe','s')
for x in [36.5,50.5,64.5,78.5]:
    arrow(ax,(x,62),(x,32),'varie')
box(ax,26,24,58,8,'resultat',label='6 + 5 + 3 + 2 = 16',size='m')
text(ax,44,19,'même reste : 1','resultat','s')
box(ax,4,4,34,10,'resultat',label='16 = 3 × 5 + 1',size='s')
box(ax,42,4,44,10,'resultat',label='6 532 = 3 × 2 177 + 1',size='s')
save(fig,'03-089')
