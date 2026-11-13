import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62); ax.set_ylim(4,66)  # cadre resserré sur le contenu (y 6→64), coordonnées de la spec inchangées

# e1 : cadre des sommes (résultats d'une addition)
box(ax,4,6,19,58,'fixe',fill=True)
text(ax,13.5,60,'sommes','fixe','s')
text(ax,13.5,56.5,'(de +)','fixe','s')

# e2 : grand cadre des produits (résultats d'une multiplication)
box(ax,26,6,60,58,'autre',fill=True)
text(ax,56,60,'produits (de ×)','autre','s')

# e3 : cadre des puissances, à l'intérieur des produits
box(ax,54,10,29,44,'sujet',fill=True)
text(ax,68.5,50,'puissances','sujet','s')
text(ax,68.5,46.5,'(facteurs égaux)','sujet','s')

# e4 : la puissance 8⁵ = 32 768, dans le cadre bleu
text(ax,68.5,36,'8 × 8 × 8 × 8 × 8','sujet','s')
disc(ax,68.5,30,1.2,'resultat')
text(ax,68.5,24,'8⁵ = 32 768','resultat','m')

# e5 : le produit 8 × 5 = 40 : hors du cadre bleu, pas une puissance de 8
disc(ax,40,30,1.2,'autre')
text(ax,40,24,'8 × 5 = 40','autre','m')
text(ax,40,18,'pas puissance de 8','limite','s')

save(fig,'04-021')
