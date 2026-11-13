import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42); ax.set_ylim(4,46)  # cadre resserré sur le contenu (y 6→42), coordonnées de la spec inchangées

# e1 : ligne du haut, exposant 3, trois facteurs 8
text(ax,8,37.5,'8','sujet','l')
text(ax,11.3,40.8,'3','varie','m')
for x in (18,30,42):
    box(ax,x,33,9,9,'sujet',label='8',size='m')

# e2 : ligne du bas, exposant 5, même base 8, trois premières cases alignées
text(ax,8,17.5,'8','sujet','l')
text(ax,11.3,20.8,'5','varie','m')
for x in (18,30,42):
    box(ax,x,13,9,9,'sujet',label='8',size='m')

# e3 : deux cases de plus, sans case au-dessus
for x in (54,66):
    box(ax,x,13,9,9,'varie',label='8',size='m')

# e4 : accolade sous les trois premières cases, 8³ = 512
brace(ax,18,51,11,'sujet',label='8³ = 512',down=True)

# e5 : accolade sous les deux cases orange, 8 × 8 = 64
brace(ax,54,75,11,'varie',label='8 × 8 = 64',down=True)

save(fig,'04-020')
