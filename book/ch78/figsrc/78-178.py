import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
xs=[5,26,47,68];ws=[16]*4
specs=[(r'$\mathbb{R}$','resultat'),(r'$\mathbb{C}$','resultat'),(r'$\times$','limite'),(r'$\mathbb{H}$','resultat')]
for i,(x,(l,r)) in enumerate(zip(xs,specs)):
    box(ax,x,24,16,12,r,label=l,size='l',dash=(r=='limite'))
    text(ax,x+8,19,f'${i+1}$','encre','s')
text(ax,44,13.5,'dimension','fixe','s')
brace(ax,5,84,39,'sujet',label='Frobenius : liste fermée',down=False)
text(ax,44,5,'Hamilton : 3 échoue, 4 réussit','fixe','s')
save(fig,'78-178')
