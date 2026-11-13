import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'le produit garde les longueurs','sujet','s')
xs=[3,35,56];ws=[26,16,28]
labs=[r'$3+4i$',r'$1+i$',r'$-1+7i$']
roles=['sujet','autre','resultat']
for x,w_,l,r in zip(xs,ws,labs,roles): box(ax,x,36,w_,11,r,label=l)
text(ax,31,41.5,r'$\times$','encre','l'); text(ax,53.5,41.5,'=','encre','l')
for x,w_,l in zip(xs,ws,['25','2','50']): box(ax,x,12,w_,11,'fixe',label=l)
text(ax,31,17.5,r'$\times$','encre','l'); text(ax,53.5,17.5,'=','encre','l')
text(ax,44,29.5,'longueur au carré','fixe','s')
text(ax,44,5,r'$25\times2=50$','resultat','m')
save(fig,'78-176')
