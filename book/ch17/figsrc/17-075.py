import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46); y=16
f=numberline(ax,10,78,y,0,20,step=1,labels=False,arrow_right=False)
ax.add_patch(Rectangle((10,y-3),f(16)-10,6,fc=FILL['resultat'],ec='none',zorder=1))
disc(ax,f(9),y,1.8,'resultat'); disc(ax,f(16),y,1.8,'fixe'); disc(ax,f(19),y,1.8,'limite')
text(ax,f(9),y-6,'9','resultat','s'); text(ax,f(16),y-6,'16','fixe','s'); text(ax,f(19),y-6,'19','limite','s')
text(ax,f(9),y+6,r'$y=5$ : vrai','resultat','s'); text(ax,f(19),y+6,r'$y=10$ : faux','limite','s')
text(ax,28,y-12,'à gauche de 16 ou égal','resultat','s')
text(ax,44,37,r'$2y-1\leq 16$','sujet','l')
save(fig,'17-075')
