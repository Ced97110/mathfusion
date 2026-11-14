import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(75)
for i in range(5):
    x=5+i*16.5
    if i==0:
        box(ax,x,40,15,14,'limite',label='0',size='l',dash=True)
    else:
        box(ax,x,40,15,14,'sujet',label=str(i),size='l')
text(ax,13,60,'pas d\'inverse','limite','s')
brace(ax,22,83,38,'sujet',label=r'$U(5)$',size='m')
text(ax,44,20,r'$2\times 3=6$, reste $1$','fixe','s')
text(ax,44,11,r'$4\times 4=16$, reste $1$','fixe','s')
save(fig,'45-047')
