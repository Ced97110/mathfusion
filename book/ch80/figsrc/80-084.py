import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
ox,oy=22,34
text(ax,22,58,'droites par l’origine','sujet','s')
import math as _m
for ang in (20,70,130):
    c,s=_m.cos(_m.radians(ang)),_m.sin(_m.radians(ang))
    line(ax,[(ox-15*c,oy-15*s),(ox+15*c,oy+15*s)],'sujet',lw=1.8)
disc(ax,ox,oy,1.3,'encre')
arrow(ax,(42,34),(51,34),'varie')
box(ax,52,14,32,40,'autre',fill=False)
text(ax,68,49,'P(V)','autre','l')
for y in (28,35,42): disc(ax,68,y,2.6,'resultat')
text(ax,68,19,'les points','resultat','s')
text(ax,44,6,'une droite = un point','fixe','s')
save(fig,'80-084')
