import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,10,54,r'$<$','sujet','xl'); text(ax,22,54,'+','encre','l'); text(ax,34,54,r'$=$','resultat','xl')
arrow(ax,(42,54),(56,54),'varie'); text(ax,70,54,r'$\leq$','sujet',14)
for i,(a,r,t) in enumerate([(7,'resultat','plus petit'),(8,'resultat','égal'),(9,'limite','faux')]):
    x=3+i*28.5
    box(ax,x,14,25,16,r,label=rf'${a}\leq8$',size='l'); text(ax,x+12.5,8,t,r,'s')
save(fig,'12-043')
