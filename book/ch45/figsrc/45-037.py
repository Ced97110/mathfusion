import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
rows=[('$3$','$8$',66),('$0$','$1$',52),('$-1$','$1/2$',38)]
for a,b,y in rows:
    box(ax,8,y-5,18,10,'sujet',label=a,size='l')
    arrow(ax,(29,y),(55,y),'varie')
    box(ax,58,y-5,22,10,'resultat',label=b,size='l')
text(ax,42,y+4.5,r'$2^x$','varie','s') if False else None
text(ax,42,71.5,r'$2^x$','varie','m')
text(ax,17,76,'réel','sujet','s'); text(ax,69,76,'image','resultat','s')
line(ax,[(8,28),(80,28)],'fixe',dash=True)
box(ax,8,6,18,14,'sujet',label=r'$x$',size='l')
arrow(ax,(29,13),(55,13),'varie')
box(ax,58,6,22,14,'resultat',label=r'$2^x$',size='l')
save(fig,'45-037')
