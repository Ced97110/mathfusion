import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,32,52,'$M$','sujet','xl'); text(ax,44,52,'/','fixe','xl'); text(ax,56,52,r'$\equiv$','varie','xl')
for x,tx,l,r in [(30,20,'le monoïde\nde départ','sujet'),(44,44,'on regroupe\nen classes','fixe'),(58,68,'la relation\nchoisie','varie')]:
    text(ax,tx,38,l,r,'s'); arrow(ax,(tx+(x-tx)*0.3,43),(x,48),r,lw=0.8)
text(ax,44,25,'deux ≡ : deux quotients','encre','m')
box(ax,2,4,40,14,'autre',label='même reste mod 3\n3 classes',size='s'); box(ax,46,4,40,14,'sujet',label='même reste mod 12\n12 classes',size='s')
save(fig,'47-112')
