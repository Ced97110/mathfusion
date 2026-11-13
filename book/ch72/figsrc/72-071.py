import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60); y=30
f=numberline(ax,12,68,y,-3,3)
line(ax,[(f(0),y-9),(f(0),y+22)],'sujet',dash=True)
text(ax,f(0),y+25,'H','sujet','m',weight='bold')
for v,r,l in ((3,'varie','(1, 2, 3)'),(0,'sujet','(1, 2, 0)'),(-3,'autre','(1, 2, −3)')):
    disc(ax,f(v),y+10,1.4,r); text(ax,f(v),y+15,l,r,'s')
text(ax,44,5,r'$B(x,u)$ : le nombre change de signe','encre','s')
save(fig,'72-071')
