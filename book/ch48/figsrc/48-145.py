import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
f1=numberline(ax,8,80,52,-2,2,labels=False,arrow_right=False)
f2=numberline(ax,8,80,14,0,3,labels=False,arrow_right=False)
text(ax,2,63,r'$x\in\mathbb{R}$','sujet','m',ha='left')
text(ax,2,21,r'$y>0$','resultat','m',ha='left')
for v,lab,r in [(-1,'−1','sujet'),(0,'0 : noyau','resultat'),(1,'1','sujet')]:
    disc(ax,f1(v),52,1.8,r); text(ax,f1(v),58,lab,r,'s')
import math
for v,lab,r in [(-1,'0,368','sujet'),(0,'1','resultat'),(1,'2,718','sujet')]:
    y=math.exp(v); disc(ax,f2(y),14,1.8,r); text(ax,f2(y),8.5,lab,r,'s')
    arrow(ax,(f1(v),49.5),(f2(y),16.5),r,lw=1.0)
text(ax,44,3,'tout y > 0 est atteint','resultat','s')
text(ax,76,40,r'$\exp$','varie','m')
save(fig,'48-145')
