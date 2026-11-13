import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
ox,oy,u=36,14,9
P=lambda x,y:(ox+u*x,oy+u*y)
line(ax,[(6,oy),(82,oy)],'fixe'); line(ax,[(ox,8),(ox,60)],'fixe')
line(ax,[P(0,0),P(4,4)],'fixe',dash=True)
n=40
line(ax,[P(-2+4*i/n,(-2+4*i/n)**2) for i in range(n+1)],'autre',lw=1.4)
line(ax,[P(4*i/n,(4*i/n)**.5) for i in range(n+1)],'sujet',lw=1.6)
arrow(ax,P(2,4),P(4,2),'varie')
text(ax,13,57,'$y=x^2$','autre','s')
text(ax,74,22,'$y=\\sqrt{x}$','sujet','s')
text(ax,72,57,'miroir : $y=x$','fixe','s')
text(ax,21,7,'carré < 0 : rien','limite','s')
text(ax,63,7,'racine d’un négatif : rien','limite','s')
arrow(ax,(33,7),(45,7),'varie',both=True)
save(fig,'22-126')
