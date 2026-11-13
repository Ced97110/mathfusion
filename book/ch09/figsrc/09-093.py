import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,40,16,12,'sujet',label='30 %')
arrow(ax,(19.5,46),(35.5,46),'varie'); text(ax,27.5,50,'décimal','varie','s',) if False else text(ax,27.5,51,'décimal','varie','s')
box(ax,36,40,16,12,'sujet',label='0,30')
arrow(ax,(52.5,46),(68.5,46),'varie'); text(ax,60.5,51,'× 50','varie','s')
box(ax,69,40,16,12,'resultat',label=r'$P$ = 15',size='s')
box(ax,3,22,60,8,'sujet',label='50'); box(ax,3,10,18,8,'resultat',label='15')
save(fig,'09-093')
