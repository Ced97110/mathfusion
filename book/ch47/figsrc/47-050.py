import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,6,8,22,48,'sujet'); box(ax,60,8,22,48,'resultat')
ys=[48,37,26,15]; vals=[0,3,6,9]
for y,v in zip(ys,vals):
    disc(ax,17,y,4,'sujet',label=str(v),size='s'); disc(ax,71,y,4,'resultat',label=str(v),size='s')
    arrow(ax,(21.8,y),(66.2,y),'varie')
text(ax,17,61,r'$N$','sujet','l'); text(ax,71,61,r'$gNg^{-1}$','resultat','l')
text(ax,44,42.5,r'$2+n-2=n$','varie','s'); text(ax,44,31.5,r'$g=2$','encre','s')
text(ax,44,3.5,r'$gNg^{-1}=N$','resultat','m')
save(fig,'47-050')
