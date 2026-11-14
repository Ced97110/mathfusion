import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
xs=[3.75+20.5*i for i in range(4)]
spec=[('étape 1','reste dans $D^*$','sujet'),('étape 2','injective','sujet'),('étape 3','tout atteint','varie'),('étape 4','1 atteint','fixe')]
for x,(a,b,role) in zip(xs,spec):
    box(ax,x,22,19,16,role,lw=1.8 if role=='varie' else 0.8)
    text(ax,x+9.5,33,a,role,'s',weight='bold'); text(ax,x+9.5,27,b,role,'s')
brace(ax,xs[0],xs[1]+19,20,'sujet',label='pas de diviseur de zéro',down=True)
brace(ax,xs[2],xs[2]+19,20,'varie',label='nombre fini',down=True)
brace(ax,xs[3],xs[3]+19,20,'fixe',label='relit 1',down=True)
save(fig,'51-235')
