import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64); ax.set_ylim(10,74)  # cadre resserré sur le contenu (y 13→72), coordonnées de la spec inchangées

# e1 : le signe en grand, la base 8
box(ax,34,50,14,18,'sujet',label='8',size='l',weight='bold')
# e2 : le petit 5, l'exposant
box(ax,49,62,8,9,'varie',label='5',size='l')

# e3 : première lecture, « huit puissance cinq », chaque mot relié à son morceau
box(ax,10,36,16,7,'sujet',label='huit',size='m')
box(ax,29,36,24,7,'fixe',label='puissance',size='m')
box(ax,56,36,14,7,'varie',label='cinq',size='m')
line(ax,[(41,50),(18,43)],'sujet',lw=0.9)
line(ax,[(53,62),(63,43)],'varie',lw=0.9)
text(ax,41,31,'comme « fois » dans 8 × 5','fixe','s')

# e5 : deuxième lecture, « huit à la cinquième »
text(ax,5,28,'ou','encre','m')
box(ax,10,17,16,7,'sujet',label='huit',size='m')
box(ax,29,17,14,7,'fixe',label='à la',size='m')
box(ax,46,17,24,7,'varie',label='cinquième',size='m')
line(ax,[(18,36),(18,24)],'sujet',dash=True)
line(ax,[(63,36),(58,24)],'varie',dash=True)

# e6 : le résultat 32 768 est la cinquième puissance de 8
arrow(ax,(57,62.5),(63.5,62.5),'resultat')
text(ax,71,59,'= 32 768','resultat','m')
text(ax,70,54,'la 5e puissance de 8','resultat','s')

save(fig,'04-022')
