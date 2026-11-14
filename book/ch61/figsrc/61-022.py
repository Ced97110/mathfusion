import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,52,r'$\mathbb{Q}(\sqrt{2})$','encre','xl')
box(ax,6,28,24,14,'fixe',label=r'$\mathbb{Q}$',size='l')
box(ax,36,28,16,14,'sujet',label='( )',size='l')
box(ax,58,28,24,14,'varie',label=r'$\sqrt{2}$',size='l')
for xc,lab,role in ((18,'les fractions','fixe'),(44,'on ajoute','sujet'),(70,'ce nombre','varie')):
    arrow(ax,(xc,28),(xc,18),role); text(ax,xc,12,lab,role,'s')
save(fig,'61-022')
