import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,54,r'$u=p+\sqrt{3}$','sujet','l'); text(ax,44,47,r'$p=1+\sqrt{2}\ \in E$','sujet')
xs=[3,24,45,66]; labs=[r'$p$',r'$1$',r'$1$',r'$\sqrt{3}$']; roles=['sujet','fixe','sujet','fixe']
for x,l,r in zip(xs,labs,roles): box(ax,x,22,14,14,r,label=l,size='l')
for x,s in [(20.5,r'$\times$'),(41.5,r'$+$'),(62.5,r'$\times$')]: text(ax,x,29,s,'encre','l')
text(ax,10,40,'coefficient','sujet','s'); text(ax,52,40,'coefficient','sujet','s')
text(ax,31,18,'base','fixe','s'); text(ax,73,18,'base','fixe','s')
save(fig,'77-109')
