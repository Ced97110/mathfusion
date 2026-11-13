import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); y=33
f=numberline(ax,12,76,y,-4,4,labels=False,arrow_right=False)
line(ax,[(f(0),y-8),(f(0),y+21)],'fixe',dash=True)
text(ax,f(0),y-11,'miroir en 0','fixe','s')
for v in (-3,-2,0,2,3): text(ax,f(v),y-4,f'{v}'.replace('-','−'),'fixe','s')
for v,r in ((3,'sujet'),(-2,'sujet'),(0,'sujet'),(-3,'resultat'),(2,'resultat')): disc(ax,f(v),y,1.6,r)
arrow(ax,(f(3),y+3),(f(-3),y+3),'varie',curve=0.3)
arrow(ax,(f(-2),y-8.5),(f(2),y-8.5),'varie',curve=0.3)
text(ax,f(0),y+17,r'$\times(-1)$','varie','m')
text(ax,44,y-22,'0 reste en 0','sujet','s')
save(fig,'17-066')
