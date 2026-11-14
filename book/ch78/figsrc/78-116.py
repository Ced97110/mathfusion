import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
labs=['0','1','2',r'$\frac{1}{2}$','…']
for i,l in enumerate(labs):
    r='limite' if i==0 else 'sujet'
    box(ax,4+i*16.5,32,14,12,r,label=l,dash=(i==0))
text(ax,11,28,'retiré','limite','s')
brace(ax,20.5,84,30,'sujet','$A^{*}$ : sans 0',down=True,depth=2.2)
brace(ax,4,84,46,'fixe','$A$',down=False,depth=2.2)
box(ax,16,2,56,9,'resultat',label=r'$2\times\frac{1}{2}=1$ : reste dans $A^{*}$')
save(fig,'78-116')
