import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,32,52,'C','sujet',22,weight='bold'); text(ax,38.5,52,'(','encre',22); text(ax,44,52,'a','fixe',22); text(ax,49.5,52,')','encre',22)
text(ax,16,30,'centralisateur','sujet','s'); text(ax,72,30,'élément fixé','fixe','s'); text(ax,44,21,'parenthèses : pas un produit','encre','s')
arrow(ax,(30,43),(20,33),'sujet'); arrow(ax,(44,43),(68,33),'fixe'); arrow(ax,(38.5,43),(38.5,24),'encre')
box(ax,10,3,68,9,'resultat',label=r'$b\in C(a)$ quand $ab=ba$',size='s')
save(fig,'45-137')
