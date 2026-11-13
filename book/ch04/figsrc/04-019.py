import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74); ax.set_ylim(3,77)  # cadre resserré sur le contenu (y 6→75), coordonnées de la spec inchangées

# e1 : trois facteurs égaux 5, base 5
text(ax,20,70,'5 × 5 × 5','sujet','l')
brace(ax,11.5,28.5,66.5,'sujet',label='3 facteurs égaux',down=True)

# e2 : la base s'écrit une seule fois, sous l'exposant
arrow(ax,(31,70),(43,70),'sujet')
text(ax,48,70,'5','sujet','l')
text(ax,51.3,73.3,'3','varie','m')
text(ax,60,64,'base : écrite une fois','sujet','s')

# e3 : produit à deux facteurs différents
text(ax,40,53,'5 × 5 × 5 × 9 × 9','fixe','m')

# e4 : écriture courte, deux bases, chacune avec son exposant
text(ax,30,42,'5','sujet','l')
text(ax,33.3,45.3,'3','varie','m')
text(ax,39,42,'×','encre','m')
text(ax,46,42,'9','autre','l')
text(ax,49.3,45.3,'2','varie','m')
text(ax,30,36,'base 5','sujet','s')
text(ax,47,36,'base 9','autre','s')

# e5 : limite, la base n'est pas le résultat
box(ax,6,8,76,12,'limite',dash=True,fill=True,label='8⁵ : base 8, résultat 32 768',size='m')

save(fig,'04-019')
