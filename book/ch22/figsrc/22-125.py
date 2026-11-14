import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
ox,oy,u=44,16,8
P=lambda x,y:(ox+u*x,oy+u*y)
box(ax,8,6,36,52,'limite',dash=True)
line(ax,[(8,oy),(80,oy)],'fixe'); line(ax,[(ox,6),(ox,58)],'fixe')
n=40
line(ax,[P(-2+4*i/n,(-2+4*i/n)**2) for i in range(n+1)],'fixe',lw=1.0)
line(ax,[P(4*i/n,(4*i/n)**.5) for i in range(n+1)],'sujet',lw=1.6)
disc(ax,P(-4,0)[0],oy,1.4,'encre',fill=False)
text(ax,26,54,'zone rouge : $x<0$','limite','s')
text(ax,22,23,'pas de point','limite','s')
text(ax,P(-4,0)[0],11,'$x=-4$','encre','s')
text(ax,ox+3,11,'0','fixe','s')
text(ax,70,53,'$y=x^2$','fixe','s')
text(ax,73,23,'$y=\\sqrt{x}$','sujet','s')
save(fig,'22-125')
