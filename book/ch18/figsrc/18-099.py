import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,56,'avec les entiers','autre','m',weight='bold'); text(ax,66,56,'avec les réels','resultat','m',weight='bold')
box(ax,6,38,32,12,'sujet',label=r'$x^2-2$',size='l'); box(ax,48,38,36,12,'resultat',label=r'$(x+\sqrt{2})(x-\sqrt{2})$',size='m')
arrow(ax,(38,44),(48,44),'varie'); text(ax,22,32,'premier','autre','m'); text(ax,66,32,'se factorise','resultat','m')
text(ax,44,19,r'pour $x=3$ :','encre','m')
text(ax,22,9,r'$9-2=7$','sujet','m'); text(ax,66,9,r'$(3+\sqrt{2})(3-\sqrt{2})=7$','resultat','s')
save(fig,'18-099')
