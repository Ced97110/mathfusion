import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
ox,oy,s=26,34,13
P=lambda a,b:(ox+a*s,oy+b*s)
line(ax,[P(-1.7,0),P(1.7,0)],'fixe'); line(ax,[P(0,-1.9),P(0,1.9)],'fixe')
disc(ax,ox,oy,2.4,'sujet')
arrow(ax,(50,44),(ox+3,oy+2),'sujet',curve=0.2)
text(ax,68,48,'le vecteur nul','sujet','s')
box(ax,50,22,34,13,'sujet',label=r'$0=\{0\}$',size='l')
text(ax,67,15,'seul vecteur : le nul','sujet','s')
text(ax,67,8,'contenu dans tous les autres','encre','s')
save(fig,'80-061')
