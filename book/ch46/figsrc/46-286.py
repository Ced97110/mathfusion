import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$A_{4}$ : 12 éléments','sujet','m')
for r_ in range(2):
    for c in range(6):
        disc(ax,12+c*12.5,34-r_*11,4,'sujet')
box(ax,4,23,80,22,'limite',fill=False,dash=True) if False else None
text(ax,44,14,r'6 divise 12 : oui','resultat','s')
text(ax,44,7,'mais aucun sous-groupe de 6','limite','s')
save(fig,'46-286')
