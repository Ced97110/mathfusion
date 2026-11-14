import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,3,12,34,36,'fixe'); text(ax,20,43,r'anneau $R$','fixe')
box(ax,8,26,24,9,'sujet',label='+ addition'); box(ax,8,15,24,9,'fixe',fill=False,dash=True,label='× produit')
arrow(ax,(39,30),(49,30),'varie'); text(ax,44,35,'on garde +','varie','s')
box(ax,51,12,34,36,'sujet',fill=False); text(ax,68,43,r'$(R,+)$','sujet')
box(ax,56,26,24,9,'sujet',label='+ addition'); text(ax,68,19,'× mise de côté','fixe','s')
box(ax,16,0.5,56,7,'resultat',label='un groupe commutatif',size='s')
save(fig,'52-033')
