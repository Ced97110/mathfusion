import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
text(ax,44,94,r'$a+(-a)=0$','encre','l')
y=68
f=numberline(ax,10,66,y,-5,5,every=5)
arrow(ax,(f(0),y+5),(f(5),y+5),'sujet'); text(ax,f(2.5),y+8,r'$a$','sujet','s')
line(ax,[(f(5),y+5),(f(5),y+11)],'fixe',dash=True)
arrow(ax,(f(5),y+11),(f(0),y+11),'varie'); text(ax,f(2.5),y+14.5,r'$-a$','varie','s')
disc(ax,f(0),y,1.5,'resultat'); text(ax,f(-3),y+8,r'$a=5$','encre','s')
y=28
g=numberline(ax,10,66,y,-5,5,every=5)
arrow(ax,(g(0),y+5),(g(-5),y+5),'varie'); text(ax,g(-2.5),y+8,r'$a$','varie','s')
line(ax,[(g(-5),y+5),(g(-5),y+11)],'fixe',dash=True)
arrow(ax,(g(-5),y+11),(g(0),y+11),'sujet'); text(ax,g(-2.5),y+14.5,r'$-a$','sujet','s')
disc(ax,g(0),y,1.5,'resultat'); text(ax,g(3),y+8,r'$a=-5$','encre','s')
save(fig,'13-061')
