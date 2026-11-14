import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[14,27,40,53,70]
text(ax,27,56,'entiers','fixe','s')
text(ax,27,24,'restes modulo 6','fixe','s')
text(ax,70,56,r'$\in (6)$','sujet','m')
for y,a,b,c in ((44,'2','3','6'),(14,r'$\bar{2}$',r'$\bar{3}$',r'$\bar{0}$')):
    box(ax,xs[0]-5,y-4.5,10,9,'sujet',label=a)
    text(ax,xs[1],y,r'$\times$','fixe','m')
    box(ax,xs[2]-5,y-4.5,10,9,'sujet',label=b)
    text(ax,xs[3],y,'=','fixe','m')
    box(ax,xs[4]-5,y-4.5,10,9,'resultat' if y<20 else 'varie',label=c)
for x in (xs[0],xs[2],xs[4]):
    arrow(ax,(x,39),(x,19.5),'varie')
save(fig,'52-103')
