import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$1 \div 3$','sujet','l')
for k in range(3):
    y=38-k*13
    box(ax,3,y,20,9,'sujet',label='reste 1',size='s')
    arrow(ax,(23.5,y+4.5),(28,y+4.5),'fixe')
    box(ax,28,y,32,9,'fixe',label=r'10 = 3$\times$3 + 1',size='s')
    arrow(ax,(60.5,y+4.5),(65,y+4.5),'fixe')
    box(ax,65,y,20,9,'resultat',label='chiffre 3',size='s')
text(ax,44,5,r'0,333$\ldots$ : le reste 1 revient','varie','s')
save(fig,'08-069')
