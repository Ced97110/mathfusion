import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
o=(44,28); u=7
c=lambda x,y,z=0: iso(x,y,z,o,u)
poly(ax,[c(-3,-3),c(3,-3),c(3,3),c(-3,3)],'sujet')
arrow(ax,c(0,0,0),c(0,0,7),'resultat',lw=1.6)
text(ax,44,19,'plan : dimension 2','sujet','m')
text(ax,66,56,'droite : dimension 1','resultat','m')
text(ax,22,76,'espace : dimension 3','encre','m')
box(ax,62,8,24,10,'resultat',label=r'$3-2=1$')
save(fig,'71-082')
