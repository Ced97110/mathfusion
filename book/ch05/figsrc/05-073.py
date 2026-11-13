import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
xs=[16,44,72]
text(ax,xs[0],46,'PGCD','sujet','xl',weight='bold')
text(ax,xs[1],46,'(12, 18)','autre','xl')
text(ax,xs[2],46,'= 6','resultat','xl',weight='bold')
for x,r,t in zip(xs,['sujet','autre','resultat'],['plus grand\ndiviseur commun','les deux nombres\ndonnés','la réponse :\nun seul nombre']):
    arrow(ax,(x,26),(x,41),r)
    box(ax,x-14,10,28,15,r,label=t,size='s')
text(ax,44,3,'PGCD(18, 12) = 6 aussi','fixe','s')
save(fig,'05-073')
