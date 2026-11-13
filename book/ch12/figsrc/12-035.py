import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
text(ax,44,43,r'$a\geq10$','sujet','xl')
f=numberline(ax,8,72,16,8,13)
arrow(ax,(f(10),28),(f(13)+5,28),'resultat')
for v,r,t in [(9,'limite','faux'),(10,'resultat','égal'),(12,'resultat','plus grand')]:
    disc(ax,f(v),16,1.7,r); text(ax,f(v),22,t,r,'s')
save(fig,'12-035')
