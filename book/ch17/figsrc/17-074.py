import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
box(ax,6,32,34,12,'varie',label=r'$2y-1$',size='l'); box(ax,42,32,16,12,'fixe',label=r'$\leq$',size='l'); box(ax,60,32,22,12,'fixe',label=r'$16$',size='l')
brace(ax,6,40,32,'varie','membre de gauche')
text(ax,23,15,r'$y=5$ : il vaut $9$','varie','s'); text(ax,23,8,r'$y=10$ : il vaut $19$','varie','s')
text(ax,66,11,'il change avec y','varie','s')
save(fig,'17-074')
