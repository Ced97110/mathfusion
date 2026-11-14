import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,68,'totaux différents','fixe','s')
box(ax,9,54,70,8,'fixe'); box(ax,9,54,70*125/160,8,'sujet',label='125 sur 160',size='s')
box(ax,9,40,35,8,'fixe'); box(ax,9,40,35*72/80,8,'autre',label='72 sur 80',size='s')
text(ax,44,32,'même total : 100','fixe','s')
box(ax,9,18,70,8,'fixe'); box(ax,9,18,70*125/160,8,'sujet',label='≈ 78 %',size='s')
box(ax,9,4,70,8,'fixe'); box(ax,9,4,63,8,'autre',label='90 %',size='s')
save(fig,'09-104')
