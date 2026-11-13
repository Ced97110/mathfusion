import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,"½ n'est pas un entier :\npermis seulement avec\ncoefficients fractionnaires",'varie','s')
arrow(ax,(35,59.5),(35,55),'varie')
box(ax,2,44,18,10,'sujet',label=r'$x-3$',size='l'); text(ax,24,49,'=','encre','l')
box(ax,28,44,14,10,'varie',label=r'$\frac{1}{2}$',size='l'); text(ax,46,49,r'$\times$','encre','l')
box(ax,50,44,26,10,'autre',label=r'$2x-6$',size='l')
text(ax,44,36,r'pour $x=5$ :','encre','m')
s=5.0
for i in range(4): ax.add_patch(Rectangle((30+i*s,20+0),s,s,ec=COL['autre'],fc=FILL['autre'],lw=0.6,zorder=2))
for i in range(2): ax.add_patch(Rectangle((30+i*s,8),s,s,ec=COL['sujet'],fc=FILL['sujet'],lw=0.6,zorder=2))
text(ax,28,22.5,r'$2x-6=4$','autre','m',ha='right'); text(ax,28,10.5,r'$x-3=2$','sujet','m',ha='right')
arrow(ax,(50,20),(40,13.5),'varie'); text(ax,66,16.5,'moitié','varie','m')
save(fig,'18-102')
