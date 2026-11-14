import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,22,62,'somme','sujet','m'); text(ax,66,62,'produit','autre','m')
for x,role,seq in [(3,'sujet',['configuration','respectée par l’iso.',"$(a+b)'=a'+b'$"]),(47,'autre',['configuration','respectée par l’iso.',"$(ab)'=a'b'$"])]:
    for i,t in enumerate(seq):
        y=46-i*16
        box(ax,x,y,38,11,role if i<2 else 'resultat',label=t,size='s')
        if i<2: arrow(ax,(x+19,y),(x+19,y-5),role)
text(ax,44,5,'même méthode, même conclusion','resultat','s')
save(fig,'80-117')
