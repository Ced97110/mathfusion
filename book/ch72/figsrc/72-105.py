import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,r=25,40,20
line(ax,[(cx-r,cy),(cx+r,cy)],'fixe',lw=0.6); line(ax,[(cx,cy-r),(cx,cy+r)],'fixe',lw=0.6)
line(ax,[(cx-r,cy-r),(cx+r,cy+r)],'limite',lw=1.4); line(ax,[(cx-r,cy+r),(cx+r,cy-r)],'limite',lw=1.4)
arrow(ax,(cx,cy),(cx+12,cy+12),'sujet'); arrow(ax,(cx,cy),(cx+12,cy),'fixe')
text(ax,cx+13,cy+15,r'$u$','sujet','m'); text(ax,cx+8,cy-3.5,r'$x$','fixe','m')
text(ax,67,56,r'$B(u,u)=1-1=0$','sujet','m'); text(ax,67,45,r'$c=2\times1\div0$','varie','m')
text(ax,67,35,'aucun nombre','limite','m'); text(ax,67,26,'pas de réflexion','limite','m')
text(ax,25,13,'droites rouges : carré nul','limite','s')
save(fig,'72-105')
