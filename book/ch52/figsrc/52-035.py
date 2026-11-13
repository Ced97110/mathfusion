import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
disc(ax,14,28,5,'sujet',label='7',size='l'); text(ax,14,19,'un élément','sujet','s')
text(ax,30,28,'∈','varie','xl'); text(ax,30,20,'appartient à','varie','s')
box(ax,44,6,42,40,'fixe'); text(ax,65,41,r'l’anneau $R$ (entiers)','fixe','s')
for (x,y,l,r) in ((52,28,'12','fixe'),(65,28,'0','fixe'),(78,28,'−3','fixe'),(65,14,'7','sujet')):
    disc(ax,x,y,4,r,label=l,size='m')
text(ax,44,50,r'$a\in R$','sujet','l')
save(fig,'52-035')
