import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42)
o=(16,8); u=24
P=lambda a,b:(o[0]+u*a,o[1]+u*b)
arrow(ax,P(0,0),P(1,0),'sujet'); arrow(ax,P(1,0),P(1,1),'sujet')
arrow(ax,P(0,0),P(0,1),'autre'); arrow(ax,P(0,1),P(1,1),'autre')
disc(ax,*P(0,0),1.6,'fixe'); disc(ax,*P(1,1),2.2,'resultat')
text(ax,28,3.5,'(1, 0)','sujet','s'); text(ax,43,20,'(0, 1)','sujet','s',ha='left')
text(ax,13,20,'(0, 1)','autre','s',ha='right'); text(ax,28,36.5,'(1, 0)','autre','s')
text(ax,46,32,'(1, 1)','resultat','s',ha='left')
text(ax,70,26,'même point','resultat','m'); text(ax,70,21,'dans les deux ordres','resultat','s')
save(fig,'49-060')
