import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,36,38,14,'sujet',label=r'$\dim(P+Q)=2$')
box(ax,47,36,38,14,'autre',label=r'$\dim(U\cap W)=1$')
text(ax,22,55,'deux points : une droite','sujet','s'); text(ax,66,55,'deux droites : un point','autre','s')
text(ax,22,31,'somme','sujet','s'); text(ax,66,31,'intersection','autre','s')
arrow(ax,(22,28),(36,17),'fixe'); arrow(ax,(66,28),(52,17),'fixe')
box(ax,14,4,60,13,'resultat',label='une seule formule, lue deux fois',size='s')
save(fig,'80-097')
