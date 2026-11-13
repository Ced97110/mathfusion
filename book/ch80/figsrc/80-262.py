import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,70,r'$\sum_{y\leq x}$','sujet','xl')
for i,x in enumerate((4,24,44,64)):
    box(ax,x,36,18,10,'resultat' if i<3 else 'limite',label='$y$ = %d'%(i+1),size='s')
brace(ax,4,62,48,'resultat',label=r'$y\leq x=3$ : comptés',down=False)
text(ax,73,29,r'$4>3$ : exclu','limite','s')
text(ax,33,24,r'$f(1)+f(2)+f(3)$','resultat','s')
save(fig,'80-262')
