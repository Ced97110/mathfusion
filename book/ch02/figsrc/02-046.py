import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
f=numberline(ax,6,82,30,0,55,5,labels=False)
a,b=f(27),f(52)
text(ax,6,26,'0','fixe','s'); text(ax,a,26,'s = 27','encre','s'); text(ax,b,26,'m = 52','encre','s')
[ax.add_patch(Circle((p,30),1.2,ec=COL['encre'],fc=COL['encre'],zorder=4)) for p in (a,b)]
ax.plot([a,b],[30,30],color=COL['sujet'],lw=3,solid_capstyle='butt',zorder=3)
mx=(a+b)/2
text(ax,mx,33.5,'d = 25','sujet','m'); text(ax,22,38,'une figure, deux lectures','sujet','s')
arrow(ax,(a,40),(b,40),'autre'); text(ax,mx,44,'27 + 25 = 52','autre','m'); text(ax,mx,49,'s + d = m','autre','s')
arrow(ax,(b,19),(a,19),'varie'); text(ax,mx,15,'52 − 27 = 25','varie','m'); text(ax,mx,10,'m − s = d','varie','s')
save(fig,'02-046')
