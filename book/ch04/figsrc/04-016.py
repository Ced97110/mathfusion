import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60); ax.set_ylim(10,70)  # cadre resserré sur le contenu (y 13→67), coordonnées de la spec inchangées

# e1 : ligne du bas, addition répétée (chapitre 3)
text(ax,22,22,'7 + 7 + 7 + 7','autre','l')
brace(ax,9.5,34.5,18.5,'autre',label='4 termes 7',down=True)

# e2 : flèche de l'addition vers l'abréviation 4 × 7
arrow(ax,(37,22),(48,22),'autre')
text(ax,52,22,'4','varie','l')
text(ax,59,22,'× 7','autre','l')

# e3 : ligne du haut, multiplication répétée
text(ax,22,58,'7 × 7 × 7 × 7','sujet','l')
brace(ax,9.5,34.5,54.5,'sujet',down=True)
text(ax,22,50.8,'4 facteurs 7','varie','s')

# e4 : flèche de la multiplication vers l'exposant 7⁴
arrow(ax,(37,58),(48,58),'sujet')
text(ax,52,58,'7','sujet','l')
text(ax,55.2,61.3,'4','varie','m')
text(ax,56,65.5,'exposant','varie','s')

# e5 : passage d'une ligne à l'autre
arrow(ax,(22,25.5),(22,48),'varie')
text(ax,25,36,'un cran plus haut','varie','s',ha='left')

# e6 : résultats, la valeur ne change pas
text(ax,70,22,'= 28','resultat','m')
text(ax,68,58,'= 2 401','resultat','m')

save(fig,'04-016')
