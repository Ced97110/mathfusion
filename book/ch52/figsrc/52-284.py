import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,24,46,40,12,'autre',label='RSA (chap. 53)')
box(ax,3,20,38,16,'sujet',label=r'inverses mod $p$',size='s'); box(ax,47,20,38,16,'sujet',label='restes chinois',size='s')
arrow(ax,(36,46),(22,36),'varie'); arrow(ax,(52,46),(66,36),'varie')
text(ax,22,13,r'$2\times3=1$ par 5','resultat','s'); text(ax,66,13,'déchiffrer, découper','varie','s')
text(ax,22,6,'par 6 : 2 sans inverse','limite','s')
save(fig,'52-284')
