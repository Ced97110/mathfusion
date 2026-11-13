import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,16,46,56,12,'sujet',label='condition d’idéal',size='m')
box(ax,3,10,38,28,'fixe'); text(ax,22,32,'normal (ch. 47)','fixe','s'); text(ax,22,24,r'$5+8=8+5$','fixe','s'); text(ax,22,16,'acquis d’office','fixe','s')
box(ax,47,10,38,28,'varie'); text(ax,66,32,'absorption','varie','s'); text(ax,66,24,r'$RI\subseteq I$','varie','s'); text(ax,66,16,'seule nouveauté','varie','s')
arrow(ax,(30,46),(22,38),'fixe'); arrow(ax,(58,46),(66,38),'fixe')
save(fig,'52-047')
