import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46); ax.set_ylim(14,60)  # cadre resserré sur le contenu (y 17→57), coordonnées de la spec inchangées
# e1 : grand 2 (facteur)
box(ax,6,24,16,22,'sujet',label='2',size='l',weight='bold')
# e2 : petit 3 (nombre de fois), en haut à droite de e1
box(ax,24,40,9,11,'varie',label='3',size='l')
# e3 : légende sous e1
text(ax,14,19,'le facteur','sujet','s')
# e4 : légende au-dessus de e2
text(ax,28.5,55,'combien de fois','varie','s')
# e5 : trois cases facteurs 2, avec × entre elles
for x in (42,58,74):
    box(ax,x,29,10,12,'sujet',label='2',size='m')
text(ax,55,35,'×','encre','m')
text(ax,71,35,'×','encre','m')
# e6 : le 2 recopié dans la première case
arrow(ax,(22,30),(41,33),'sujet')
# e7 : accolade sur les trois cases
brace(ax,42,84,44,'varie',label='3 facteurs 2',down=False)
# e8 : du petit 3 vers l'accolade
arrow(ax,(34,45.5),(41,45.5),'varie')
# e9 : flèche vers le résultat
arrow(ax,(63,28.5),(63,22.5),'resultat')
text(ax,63,20,'puis on multiplie : 8','resultat','m')
save(fig,'04-012')
