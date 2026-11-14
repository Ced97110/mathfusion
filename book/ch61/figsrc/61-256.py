import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(58)
poly(ax,[(30,10),(48,28),(30,46),(12,28)],'resultat')
poly(ax,[(30,10),(48,10),(48,28),(30,28)],'sujet')
line(ax,[(30,10),(48,28)],'varie',lw=1.6)
text(ax,68,50,'côté 1 cm','sujet','m'); text(ax,68,45,'aire 1 cm²','sujet','m')
text(ax,68,35,'diagonale ≈ 1,414 cm','varie','s')
text(ax,68,25,'nouveau carré :','resultat','m'); text(ax,68,20,'côté = diagonale','resultat','s'); text(ax,68,15,'aire ≈ 2 cm²','resultat','m')
save(fig,'61-256')
