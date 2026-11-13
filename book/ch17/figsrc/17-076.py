import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,6,52,34,10,'fixe',label=r'$2y-1$',size='m'); box(ax,42,52,16,10,'fixe',label=r'$\leq$',size='m'); box(ax,60,52,22,10,'sujet',label=r'$16$',size='m')
brace(ax,60,82,52,'sujet','membre de droite')
text(ax,23,37,'gauche','varie','s'); text(ax,71,37,'droite','sujet','s')
for yy,a,l in ((24,'9','y = 5'),(10,'19','y = 10')):
    box(ax,12,yy,22,9,'varie',label=f'${a}$',size='m'); box(ax,60,yy,22,9,'sujet',label='$16$',size='m'); text(ax,44,yy+4.5,f'${l[0]}{l[1:]}$','fixe','s')
save(fig,'17-076')
