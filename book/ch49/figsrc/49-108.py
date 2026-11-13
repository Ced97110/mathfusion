import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
box(ax,2,24,12,14,'sujet',label=r'$g$',size='l')
arrow(ax,(14,31),(32,31),'varie')
text(ax,23,35,r'$T$','varie','m')
xs=[40,58,76]
for x,l in zip(xs,'123'): disc(ax,x,31,4,'fixe',label=l)
arrow(ax,(44.5,31),(53.5,31),'sujet',both=True)
text(ax,76,22,'reste','fixe','s')
text(ax,58,44,r'$T(g)$ : échange 1 et 2, fixe 3','sujet','s')
text(ax,44,11,r'$gx = T(g)x$','resultat','l',weight='bold')
text(ax,44,4,r'$g$ agit comme la bijection $T(g)$','resultat','s')
save(fig,'49-108')
