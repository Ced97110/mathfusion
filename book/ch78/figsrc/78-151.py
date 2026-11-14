import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
ox,oy=12,14
arrow(ax,(ox,oy),(84,oy),'fixe'); arrow(ax,(ox,oy),(ox,74),'sujet')
text(ax,80,oy-4,r'$\mathbb{R}$','fixe','m'); text(ax,ox+8,72,r"$A'$",'sujet','m')
px,py=ox+40,oy+34
line(ax,[(px,oy),(px,py)],'fixe',dash=True); line(ax,[(ox,py),(px,py)],'sujet',dash=True)
disc(ax,px,py,2,'resultat')
text(ax,px+6,py+5,r'$x=a+y$','resultat','m')
text(ax,px,oy-4,r'$a=3$','fixe','m')
text(ax,ox+14,py+4,r'$y=2i$','sujet','m')
text(ax,48,4,r"$A=\mathbb{R}\oplus A'$ : une seule écriture",'encre','s')
save(fig,'78-151')
