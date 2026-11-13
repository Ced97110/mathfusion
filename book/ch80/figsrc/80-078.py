import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(64)
text(ax,22,59,'espace vectoriel','fixe','m')
text(ax,66,59,'espace projectif','fixe','m')
line(ax,[(6,10),(38,46)],'sujet',lw=1.8)
for t in (0.2,0.45,0.7,0.92):
    disc(ax,6+32*t,10+36*t,1.2,'sujet')
text(ax,22,52,'droite de vecteurs','sujet','s')
arrow(ax,(42,30),(54,30),'varie')
text(ax,48,34.5,'se lit','varie','s')
disc(ax,70,30,4.5,'resultat')
text(ax,70,19,'un seul point','resultat','m')
save(fig,'80-078')
