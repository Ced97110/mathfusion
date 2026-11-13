import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,4,24,28,35,'sujet',fill=True)
text(ax,18,53,r'$\{1\}$','sujet','m'); disc(ax,18,38,6,'sujet',label='1',size='l')
for y,s,r in ((52,r'produit : $1\cdot1=1$','resultat'),(41,'neutre : 1','sujet'),(30,r'inverse : $1^{-1}=1$','sujet')):
    arrow(ax,(24.5,38),(37,y),'fixe'); text(ax,39,y,s,r,'m',ha='left')
box(ax,4,4,28,15,'limite',fill=False,dash=True); text(ax,18,11.5,r'$\varnothing$','limite','l')
text(ax,39,11.5,'vide : pas de neutre','limite','m',ha='left')
save(fig,'44-263')
