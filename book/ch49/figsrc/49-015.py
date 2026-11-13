import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
disc(ax,14,33,3.6,'resultat',label='1',size='s')
disc(ax,44,33,3.6,'sujet',label='$x$',size='s')
disc(ax,70,33,2.3,'sujet'); disc(ax,44,55,2.3,'autre'); disc(ax,44,11,2.3,'autre')
arrow(ax,(17.8,33),(40,33),'sujet',lw=1.3); text(ax,29,29.2,'$x$','sujet','m')
arrow(ax,(47.8,33),(67.4,33),'sujet',lw=1.3)
arrow(ax,(44,37.2),(44,52.3),'autre'); text(ax,48,45,'$y$','autre','m')
arrow(ax,(44,28.8),(44,13.7),'autre'); text(ax,49,21,'$y^{-1}$','autre','s')
# missing arrow x^-1 : from x back to the centre, dashed red, crossed out
arrow(ax,(41,36),(16.5,36.5),'limite',curve=0.45,lw=1.2)
ax.patches[-1].set_linestyle('--')
mx,my=28.7,41.9
line(ax,[(mx-2,my-2),(mx+2,my+2)],'limite',lw=1.4); line(ax,[(mx-2,my+2),(mx+2,my-2)],'limite',lw=1.4)
text(ax,29,47.5,'$x^{-1}$','limite','m')
text(ax,29,54,'retour au centre','limite','s')
text(ax,14,24,'déjà atteint','resultat','s')
text(ax,14,12,'$x\\,x^{-1}=1$','resultat','m')
save(fig,'49-015')
