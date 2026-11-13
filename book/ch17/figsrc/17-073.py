import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
box(ax,6,24,34,12,'varie',label=r'$2y-1$',size='l'); box(ax,42,24,16,12,'sujet',label=r'$\leq$',size='l'); box(ax,60,24,22,12,'fixe',label=r'$16$',size='l')
brace(ax,6,40,24,'varie','membre de gauche'); brace(ax,42,58,24,'sujet','symbole'); brace(ax,60,82,24,'fixe','membre de droite')
text(ax,23,8,'2 fois y moins 1','varie','s'); text(ax,50,8,'inférieur ou égal à','sujet','s'); text(ax,71,8,'16','fixe','s')
save(fig,'17-073')
