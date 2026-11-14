import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,22,65,'les cinq axiomes','fixe','s'); text(ax,66,65,'absents de la liste','autre','s')
for i in range(5): box(ax,10,52-i*10-4,24,9,'fixe',label='A%d'%(i+1))
box(ax,48,40,38,14,'autre',fill=False,dash=True,label=r'$a\vee a=a$'); text(ax,67,36,'idempotence','autre','s')
box(ax,48,16,38,14,'autre',fill=False,dash=True,label=r'$a\leq b$'); text(ax,67,12,'ordre','autre','s')
save(fig,'80-151')
