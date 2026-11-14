import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
xs=[26,42,58,74]
for x,l in zip(xs,'1234'):
    disc(ax,x,40,4,'fixe',label=l)
    arrow(ax,(x,35.2),(x,22.8),'varie')
    disc(ax,x,18,4,'resultat',label=l)
text(ax,8,40,r'$x$','sujet','l'); text(ax,8,18,r'$1x$','resultat','l')
text(ax,8,29,'neutre','varie','s')
text(ax,44,6,r'$1x = x$ pour chaque point','resultat','m',weight='bold')
save(fig,'49-099')
