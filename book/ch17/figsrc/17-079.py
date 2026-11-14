import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72); y=56
f=numberline(ax,10,78,y,-3,3,labels=False,arrow_right=False)
ax.add_patch(Rectangle((10,y-3),f(0)-10,6,fc=FILL['limite'],ec='none',zorder=1))
disc(ax,f(-1),y,1.8,'varie'); text(ax,f(-1),y+5,r'$d=-1$','varie','s'); text(ax,f(0),y-5,'$0$','fixe','s'); text(ax,f(-2),y-5,'$d<0$','limite','s')
box(ax,4,16,38,20,'resultat'); box(ax,46,16,38,20,'limite')
text(ax,23,31,'prix : 3 + 2d','resultat','s'); text(ax,23,22,'1 ≤ 15 : accepté','resultat','s')
text(ax,65,31,'distance : d ≥ 0','limite','s'); text(ax,65,22,'−1 ≥ 0 : faux','limite','s')
arrow(ax,(f(-1)-1,y-4),(23,37.5),'varie'); arrow(ax,(f(-1)+1,y-4),(65,37.5),'varie')
text(ax,44,6,'les deux doivent être vraies','fixe','s')
save(fig,'17-079')
