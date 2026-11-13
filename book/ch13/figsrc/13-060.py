import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
y=54
f=numberline(ax,8,68,y,0,6,every=1)
disc(ax,f(5),y,1.7,'resultat')
text(ax,f(5),y+7,r'$5+0=5$','resultat','s')
text(ax,36,y+15,r'0 pas : $a+0=a$, 0 est neutre','varie','s')
box(ax,4,8,38,16,'limite',label=r'$5\times0=0$')
box(ax,46,8,38,16,'resultat',label=r'$5\times1=5$')
text(ax,23,30,'0 n’est pas neutre pour $\\times$','limite','s')
text(ax,65,30,'1 est neutre pour $\\times$','resultat','s')
save(fig,'13-060')
