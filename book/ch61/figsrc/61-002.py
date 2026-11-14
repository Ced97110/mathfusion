import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(46)
A=(30,22); B=(58,22)
line(ax,[(5,22),(83,22)],'sujet',lw=1.3)
arrow(ax,(70,22),(84,22),'sujet',lw=1.3); arrow(ax,(18,22),(4,22),'sujet',lw=1.3)
disc(ax,*A,1.5,'fixe'); disc(ax,*B,1.5,'fixe')
text(ax,30,26.5,'A','encre'); text(ax,58,26.5,'B','encre')
brace(ax,30,58,18,'fixe','1 cm')
text(ax,44,36,'droite AB','sujet','l')
text(ax,13,29,'le trait dépasse','varie','s'); text(ax,74,29,'des deux côtés','varie','s')
save(fig,'61-002')
