import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86); ax.set_ylim(11,97)  # cadre resserré sur le contenu (y 15→94), coordonnées de la spec inchangées

# e1 : le produit de cinq facteurs 8, et l'accolade qui compte 5
text(ax,44,92,'8 × 8 × 8 × 8 × 8','varie','l')
brace(ax,28,60,88,'varie',label='① compter : 5 facteurs',down=True)

# e2 : action 2, écrire le 8 une seule fois
arrow(ax,(62,83),(66,75),'sujet')
text(ax,6,72,'② écrire le 8 une fois','encre','s',ha='left')
text(ax,66,72,'8','sujet','l')

# e3 : action 3, écrire le 5 en petit, en haut à droite
arrow(ax,(66,69.5),(66,61.5),'varie')
text(ax,6,58,'③ écrire 5 en petit, en haut','encre','s',ha='left')
text(ax,66,58,'8','sujet','l')
text(ax,69.3,61.3,'5','varie','m')

# e4 : calcul de gauche à droite, quatre cases et trois flèches
text(ax,6,44,'④ fois 8, de gauche à droite','encre','s',ha='left')
box(ax,10,30,10,8,'fixe',label='64',size='m')
box(ax,25,30,11,8,'fixe',label='512',size='m')
box(ax,41,30,14,8,'fixe',label='4 096',size='m')
box(ax,60,30,17,8,'resultat',label='32 768',size='m')
arrow(ax,(20,34),(25,34),'varie')
arrow(ax,(36,34),(41,34),'varie')
arrow(ax,(55,34),(60,34),'varie')

# e5 : égalité finale
text(ax,44,16,'même nombre : 8⁵ = 32 768','resultat','m')

save(fig,'04-018')
