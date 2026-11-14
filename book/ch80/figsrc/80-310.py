import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
O=(20,18); s=8
line(ax,[(2,O[1]),(58,O[1])],'sujet',0.8); line(ax,[(12,10),(58,56)],'autre',0.8)
arrow(ax,O,(O[0]+s,O[1]),'fixe',1.0); arrow(ax,O,(O[0]+4*s,O[1]),'sujet',1.5)
arrow(ax,O,(O[0]+s,O[1]+s),'fixe',1.0); arrow(ax,O,(O[0]+4*s,O[1]+4*s),'autre',1.5)
line(ax,[(52,19.5),(52,48.5)],'limite',1.0,dash=True); text(ax,52,34,r'$\times$','limite','xl')
text(ax,28,13.5,'(1, 0)','fixe','s'); text(ax,52,13.5,'(4, 0)','sujet','s')
text(ax,36,23,'(1, 1)','fixe','s'); text(ax,63,49,'(4, 4)','autre','s')
text(ax,72,38,'échange voulu :\nimpossible','limite','s')
text(ax,30,58,r'$\eta(v)=4v$ : chaque flèche reste','encre','s')
text(ax,44,4,'les pentes 0 et 1 restent en place','resultat','s')
save(fig,'80-310')
