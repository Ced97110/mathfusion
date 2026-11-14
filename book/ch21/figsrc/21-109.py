import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
Y=[56,45,34,23,12]
N=[(r'$x^2+5x+6$',27,'sujet'),(r'$-(x^2+2x)$',24,'varie'),(r'$3x+6$',27,'sujet'),(r'$-(3x+6)$',27,'varie'),(r'$0$',27,'resultat')]
for (s,x,r),y in zip(N,Y): text(ax,x,y,s,r,'m',ha='right')
line(ax,[(30,60),(30,51)],'fixe'); line(ax,[(30,51),(44,51)],'fixe')
text(ax,37,56,r'$x+2$','autre','m'); text(ax,37,45,r'$x+3$','resultat','m')
line(ax,[(4,39.5),(28,39.5)],'fixe'); line(ax,[(4,17.5),(28,17.5)],'fixe')
L=[r'$x^2\div x=x$',r'$x\,(x+2)=x^2+2x$',r'reste $3x+6$',r'$3x\div x=3$, puis $3(x+2)$',r'reste 0, quotient $x+3$']
R=['varie','varie','sujet','varie','resultat']
for s,r,y in zip(L,R,Y): text(ax,48,y,s,r,'s',ha='left')
save(fig,'21-109')
