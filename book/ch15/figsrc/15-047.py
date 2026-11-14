import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plus(ax,x,y,role="fixe",s=1.4):
    line(ax,[(x-s,y),(x+s,y)],role,lw=1.1); line(ax,[(x,y-s),(x,y+s)],role,lw=1.1)
fig,ax=canvas(84)
text(ax,4,78,r'$x=3$','fixe','m',ha='left')
box(ax,4,62,14,11,'sujet',label=r'$8x$',size='l'); plus(ax,22,67.5); box(ax,26,62,14,11,'sujet',label=r'$5x$',size='l')
box(ax,4,38,36,11,'varie',label=r'$(8+5)x$',size='l'); box(ax,4,14,36,11,'resultat',label=r'$13x$',size='l')
arrow(ax,(22,62),(22,49),'varie'); text(ax,26,55.5,r'$x$ commun','varie','s',ha='left')
arrow(ax,(22,38),(22,25),'varie'); text(ax,26,31.5,r'$8+5=13$','varie','s',ha='left')
text(ax,66,67.5,r'$24+15=39$','sujet','m'); text(ax,66,19.5,r'$13\times3=39$','resultat','m')
save(fig,'15-047')
