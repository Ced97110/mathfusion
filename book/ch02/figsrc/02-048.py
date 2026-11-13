import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,53,'ajouter 4, puis retirer 4','encre','m')
f=numberline(ax,6,82,30,0,16,1,labels=False)
for s,cx in ((2,25),(10,63)):
    a,b=f(s),f(s+4)
    line(ax,[(a,30),(a,11)],'resultat',dash=True)
    disc(ax,a,30,1.5,'resultat'); text(ax,a,9,'départ','resultat','s')
    arrow(ax,(a,31.5),(b,31.5),'autre',curve=-0.8); text(ax,cx,43,'+ 4','autre','m')
    disc(ax,b,30,1,'fixe')
    arrow(ax,(b,28.5),(a,28.5),'varie',curve=-0.8); text(ax,cx,17,'− 4','varie','m')
text(ax,44,3.5,'retour au départ, partout','resultat','s')
save(fig,'02-048')
