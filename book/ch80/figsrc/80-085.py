import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(58)
rows=[('dim 0 : origine seule',46,'fixe'),('dim 1 : droite par l’origine',34,'sujet'),('dim 2 : plan par l’origine',22,'fixe'),('dim 3 : espace entier',10,'fixe')]
for lab,y,role in rows: box(ax,3,y,46,9,role,label=lab,size='s')
arrow(ax,(50,38.5),(60,38.5),'varie')
text(ax,55,42.5,'on dit','varie','s')
box(ax,61,34,24,9,'resultat',label='point',size='m')
save(fig,'80-085')
