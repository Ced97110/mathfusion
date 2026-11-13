import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
poly(ax,[(6,10),(54,10),(70,40),(22,40)],'sujet',lw=1.0)
for a,b in [((14,25),(62,25)),((26,13),(50,37)),((46,13),(30,37))]:
    line(ax,[a,b],'sujet',lw=1.6)
disc(ax,38,25,1.5,'encre')
text(ax,38,46,'plan par l’origine (dim 2)','sujet','s')
text(ax,38,57,'droite projective','resultat','l')
arrow(ax,(38,53.2),(38,49.2),'resultat')
text(ax,44,4,'chaque droite par l’origine = un point','fixe','s')
save(fig,'80-080')
