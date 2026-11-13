import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54); ax.set_ylim(2,56)  # cadre resserré sur le contenu (y 6→52), coordonnées de la spec inchangées

# e1 : séparation entre facteur (gauche) et exposant (droite)
line(ax,[(43,4),(43,52)],'fixe',dash=True)

# e2 : colonne gauche, 8 × 5 (5 à côté de 8)
text(ax,22,47,'8 × 5','autre','l')
text(ax,22,41,'5 à côté','fixe','s')

# e3 : colonne droite, 8⁵ (5 en petit, en haut à droite)
text(ax,60,47,'8','sujet','l')
text(ax,63.3,50.3,'5','varie','m')
text(ax,64,41,'5 en haut à droite','fixe','s')

# e4 : le 5 est un facteur : 40 carrés, grille 8 colonnes × 5 lignes
text(ax,22,36,'5 est un facteur','autre','s')
for c in range(8):
    for r in range(5):
        box(ax,12+c*2.5,16+r*2.5,2.5,2.5,'autre',label=None,r=0.2)

# e5 : le 5 est un exposant : 5 facteurs 8
text(ax,64,36,'5 compte les facteurs 8','varie','s')
text(ax,64,27,'8 × 8 × 8 × 8 × 8','sujet','m')
brace(ax,50.5,77.5,24,'varie',label='5 facteurs 8',down=True)

# e6 : deux résultats différents
text(ax,22,8,'8 × 5 = 40','resultat','m')
text(ax,64,8,'8⁵ = 32 768','resultat','m')

save(fig,'04-017')
