import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
text(ax,44,40,r'$q=7$','encre','l')
xs=[2,34,66]; labs=['2 016','336','168']; roles=['fixe','fixe','resultat']
caps=['inversibles (48 × 42)','déterminant 1',r'ordre de $PSL$']
for x,l,r,c in zip(xs,labs,roles,caps):
    box(ax,x,16,20,12,r,label=l,size='l'); text(ax,x+10,11,c,r,'s')
for i,(a,b) in enumerate([('÷ 6',r'$q-1$'),('÷ 2','pgcd 2')]):
    x0=xs[i]+20; x1=xs[i+1]
    arrow(ax,(x0,22),(x1,22),'varie'); text(ax,(x0+x1)/2,26,a,'varie','m'); text(ax,(x0+x1)/2,18,b,'varie','s')
save(fig,'73-177')
