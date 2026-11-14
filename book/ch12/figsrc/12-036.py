import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
text(ax,44,43,r'$a\leq50$','sujet','xl')
f=numberline(ax,14,74,16,48,53)
arrow(ax,(f(50),28),(6,28),'resultat')
for v,r,t in [(49,'resultat','plus petit'),(50,'resultat','égal'),(51,'limite','faux')]:
    disc(ax,f(v),16,1.7,r); text(ax,f(v),22,t,r,'s')
save(fig,'12-036')
