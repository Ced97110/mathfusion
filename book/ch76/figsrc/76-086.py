import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
labs=['1',r'$e_1$',r'$e_2$',r'$e_1 e_2$']; roles=['fixe','sujet','sujet','varie']
for i,(l,r) in enumerate(zip(labs,roles)):
    box(ax,7+i*20,22,16,12,r,label=l,size='m')
brace(ax,7,83,36,'resultat',r'$\Lambda(V)$',down=False,size='l')
brace(ax,27,63,20,'sujet','$V$',down=True,size='m')
text(ax,75,13,'produit','varie','s')
arrow(ax,(75,16),(75,21),'varie')
save(fig,'76-086')
