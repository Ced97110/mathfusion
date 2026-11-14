import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cx,cy,u=26,50,18
line(ax,[(cx-6,cy),(cx+30,cy)],'fixe',lw=0.6); line(ax,[(cx,cy-6),(cx,cy+28)],'fixe',lw=0.6)
arrow(ax,(cx,cy),(cx+u,cy),'sujet'); arrow(ax,(cx,cy),(cx,cy+u),'autre'); arrow(ax,(cx,cy),(cx+u,cy+u),'resultat')
line(ax,[(cx+u,cy),(cx+u,cy+u),(cx,cy+u)],'fixe',dash=True,lw=0.6)
text(ax,cx+u/2,cy-3,r'$x$','sujet'); text(ax,cx-3,cy+u/2,r'$y$','autre'); text(ax,cx+u+2.5,cy+u+3,r'$x+y$','resultat',ha='left')
text(ax,66,cy-3,'carré 1','sujet'); text(ax,66,cy+7,'carré 1','autre'); text(ax,66,cy+17,'carré 2','resultat')
text(ax,44,28,r'$B(x,y)=\frac{1}{2}\,(2-1-1)$','encre','m')
text(ax,44,17,r'$B(x,y)=0$','resultat','l')
text(ax,44,7,'le carré de la somme suffit','fixe','s')
save(fig,'72-099')
