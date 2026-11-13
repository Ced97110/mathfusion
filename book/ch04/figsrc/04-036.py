import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(60)

# nombre de départ : une rangée de 4 carrés
for i in range(4):
    box(ax, 10 + i * 4.5, 30, 4, 4, 'sujet', r=0.5)
text(ax, 18.75, 40, '4', 'sujet', 'l')
text(ax, 18.75, 18, 'racine = origine', 'sujet', 's')
text(ax, 18.75, 13, 'nombre de départ', 'sujet', 's')

# action : la flèche part du bord de la rangée et arrive au bord de la grille
arrow(ax, (27.5, 32), (54, 32), 'varie', lw=1.2)
text(ax, 40.75, 37, 'fois lui-même', 'varie', 's')

# nombre d'arrivée : grille 4 × 4
for i in range(4):
    for j in range(4):
        box(ax, 54 + i * 4.5, 23.25 + j * 4.5, 4, 4, 'resultat', r=0.5)
text(ax, 62.75, 47, '16', 'resultat', 'l')
text(ax, 62.75, 18, 'puissance', 'resultat', 's')
text(ax, 62.75, 13, 'nombre d’arrivée', 'resultat', 's')

# le signe √ fait le chemin inverse : de 16 il retrouve le départ, la racine
arrow(ax, (60, 22), (22, 28.5), 'fixe', lw=0.9, curve=-0.25)
text(ax, 41, 17.5, 'retour : √16 = 4', 'fixe', 's')

# les deux mots désignent les deux nombres d'un seul calcul
brace(ax, 8, 74, 52, 'fixe', label='un même calcul : 4 × 4 = 16', down=False, size='s')

save(fig, '04-036')
