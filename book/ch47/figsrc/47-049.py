import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,r'$g^{-1}\,n\,g$','sujet','xl')
cx=[18,44,70]; labs=[r'$g^{-1}$',r'$n$',r'$g$']; roles=['varie','sujet','varie']
for c,l,r in zip(cx,labs,roles): box(ax,c-10,34,20,12,r,label=l,size='l')
arrow(ax,(60,40),(54.5,40),'varie'); arrow(ax,(34,40),(28.5,40),'varie')
for c,t in zip(cx,['3 : en dernier','2 : puis',"1 : d'abord"]): text(ax,c,28,t,'fixe','s')
text(ax,44,17,r'$g=s$ et $n=r$','encre','m')
text(ax,44,8,r'$s^{-1}rs=r^{3}$','resultat','l')
save(fig,'47-049')
