import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,54,'horloge à 10 heures','fixe','m')
inv={1,3,7,9}; xs=[8+8*i for i in range(10)]
for i,x in enumerate(xs):
    disc(ax,x,40,3.3,'sujet' if i in inv else 'fixe',label=str(i),size='s')
box(ax,16,6,56,11,'resultat',label=r'$U(10)=\{1,3,7,9\}$',size='m')
tx=[32,41,50,59]
for i,t in zip(sorted(inv),tx): arrow(ax,(xs[i],36.4),(t,18),'sujet')
save(fig,'47-051')
