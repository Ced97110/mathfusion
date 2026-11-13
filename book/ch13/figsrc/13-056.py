import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y=24
f=numberline(ax,6,70,y,-14,2,every=7)
arrow(ax,(f(0),y+5),(f(-4),y+5),'varie'); text(ax,f(-2),y+8,'4 pas','varie','s')
line(ax,[(f(-4),y+5),(f(-4),y+10)],'fixe',dash=True)
arrow(ax,(f(-4),y+10),(f(-13),y+10),'varie'); text(ax,f(-8.5),y+13.5,'9 pas','varie','s')
disc(ax,f(-13),y,1.7,'resultat'); text(ax,f(-13)+1,y+5,r'$-13$','resultat','s')
brace(ax,f(-13),f(0),y-6,'resultat',label=r'$13=4+9$')
text(ax,44,y+22,r'$(-4)+(-9)$ : même sens','encre','s')
save(fig,'13-056')
