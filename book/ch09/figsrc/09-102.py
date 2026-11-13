import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for y,l,r in ((52,'24,95 $','sujet'),(30,'21,2075 $','fixe'),(8,'21,21 $','resultat')):
    box(ax,30,y,30,10,r,label=l,size='m')
arrow(ax,(45,52),(45,41),'varie'); arrow(ax,(45,30),(45,19),'varie')
text(ax,49,46.5,r'$\times\ 0{,}85$','varie','s',ha='left'); text(ax,49,24.5,'arrondi au centime','varie','s',ha='left')
text(ax,27,57,'prix','sujet','s',ha='right'); text(ax,27,35,'exact','fixe','s',ha='right'); text(ax,27,13,'à payer','resultat','s',ha='right')
save(fig,'09-102')
