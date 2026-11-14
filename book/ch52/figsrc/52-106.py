import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
cols=[(15,'commutatif',r'$\mathbb{Z}$ : $ab=ba$','matrices : ab ≠ ba'),(44,'unité 1',r'$\mathbb{Z}$ : 1 existe','matrices : 1 existe'),(73,'1 ≠ 0',r'$\mathbb{Z}$ : 1 ≠ 0','anneau {0} : 1 = 0')]
for cx,h,ok,ko in cols:
    text(ax,cx,50,h,'sujet','m')
    box(ax,cx-13.5,32,27,10,'resultat',label=ok,size='s')
    if ko: box(ax,cx-13.5,14,27,10,'resultat' if 'existe' in ko else 'limite',label=ko,size='s')
text(ax,44,5,'trois exigences sur R','fixe','s')
save(fig,'52-106')
