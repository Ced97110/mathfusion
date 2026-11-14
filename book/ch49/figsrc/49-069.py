import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,12,39,46,'fixe'); text(ax,22.5,52,'groupe libre','fixe','m')
box(ax,46,12,39,46,'sujet'); text(ax,65.5,52,'groupe du carré','sujet','m')
text(ax,22.5,38,r'$x^4 \neq 1$','limite','l'); text(ax,22.5,24,r'$y^2 \neq 1$','limite','l')
text(ax,65.5,38,r'$x^4 = 1$','resultat','l'); text(ax,65.5,24,r'$y^2 = 1$','resultat','l')
arrow(ax,(43,31),(45,31),'varie')
brace(ax,46,85,12,'resultat','relations : mots égaux à 1')
save(fig,'49-069')
