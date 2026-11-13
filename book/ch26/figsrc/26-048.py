import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
box(ax,4,28,30,14,'sujet',label='60,07°',size='m')
box(ax,54,28,30,14,'autre',label=r'$0{,}8666\ldots$',size='m')
text(ax,19,46,'angle','sujet','s'); text(ax,69,46,'nombre','autre','s')
arrow(ax,(35,38),(53,38),'fixe'); text(ax,44,41.5,'sin','fixe','s')
arrow(ax,(53,32),(35,32),'varie'); text(ax,44,28.5,'arcsin','varie','s')
box(ax,9,6,70,12,'resultat',label=r'$\theta=\arcsin(0{,}8666\ldots)$',size='m')
save(fig,'26-048')
