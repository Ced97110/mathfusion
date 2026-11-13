import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72); ax.set_ylim(3,75)  # cadre resserré sur le contenu (y 6→72), coordonnées de la spec inchangées
# e1 : carré de côté 5, 25 carreaux, et son accolade
for x in (6,11,16,21,26):
    for y in (40,45,50,55,60):
        box(ax,x,y,5,5,'sujet')
brace(ax,6,31,67,'sujet',label='côté 5',down=False)
# e2 : compte exact des carreaux
text(ax,18.5,34,'5² = 25 carreaux','resultat','m')
# e3 : cube de côté 5, 125 petits cubes (3D exacte)
cubes(ax,[(i,j,k) for i in range(5) for j in range(5) for k in range(5)],(62,38),3,'sujet')
text(ax,81,52,'côté 5','sujet','s')
# e4 : compte exact des petits cubes
text(ax,62,34,'5³ = 125 petits cubes','resultat','m')
# e5 : limite, pour un petit 4 aucune forme
box(ax,6,6,76,18,'limite',dash=True,fill=True)
text(ax,44,19,'2⁴ = 2 × 2 × 2 × 2 = 16','limite','m')
text(ax,44,11,"aucune forme de l'espace",'limite','m')
save(fig,'04-015')
