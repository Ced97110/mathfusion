import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
box(ax,6,24,76,54,'resultat',fill=False,dash=True)
disc(ax,33,46,18,'sujet',fill=False,lw=1.2)
disc(ax,55,46,18,'autre',fill=False,lw=1.2)
text(ax,25,46,'3','sujet','m'); text(ax,44,46,'2','encre','m'); text(ax,63,46,'5','autre','m')
text(ax,27,72,r'$\varphi$(6)','sujet','s'); text(ax,61,72,r'$\varphi$(10)','autre','s')
text(ax,44,13,r'$\varphi$(30) = {2, 3, 5} : l’union','resultat','s')
save(fig,'80-248')
