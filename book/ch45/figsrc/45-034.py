import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
text(ax,22,89,'Entiers','sujet','m',weight='bold')
text(ax,66,89,'Arrivée','fixe','m',weight='bold')
ys=[80,68,56,44]; vals=['$-1$','$0$','$1$','$2$']
for y,v in zip(ys,vals):
    role='limite' if v=='$1$' else 'sujet'
    disc(ax,22,y,4.5,role if role=='limite' else 'sujet',label=v)
    arrow(ax,(27.5,y),(58,62-(62-y)*0.25),role)
disc(ax,66,62,5.5,'fixe',label='$0$')
box(ax,4,26,38,9,'resultat',label=r'sommes gardées',size='s')
box(ax,46,26,38,9,'limite',label=r'$1\mapsto 0$, pas $1\mapsto 1$',size='s')
text(ax,44,16,'la condition sur 1 reste utile','encre','m',weight='bold')
save(fig,'45-034')
