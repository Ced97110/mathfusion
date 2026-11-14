import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,57,r'« ajouter 1 »','limite','m'); text(ax,66,57,'identité','resultat','m')
box(ax,3,28,38,22,'limite',label=None); box(ax,47,28,38,22,'resultat',label=None)
text(ax,22,44,r'$\sigma(2+3)=6$','limite'); text(ax,22,34,r'$\sigma(2)+\sigma(3)=7$','limite')
text(ax,66,44,r'$\sigma(2+3)=5$','resultat'); text(ax,66,34,r'$\sigma(2)+\sigma(3)=5$','resultat')
box(ax,3,6,38,12,'limite',label=r'$6\neq 7$'); box(ax,47,6,38,12,'resultat',label=r'$5=5$')
text(ax,22,22,'bijection, mais refusée','limite','s'); text(ax,66,22,'respecte la somme','resultat','s')
save(fig,'80-098')
