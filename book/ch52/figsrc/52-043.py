import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,3,30,82,40,'sujet',fill=False); text(ax,44,65,r'idéal $I$','sujet')
box(ax,8,40,34,14,'fixe',label=r'sous-groupe de $(R,+)$',size='s'); text(ax,46,47,'+','encre','l')
box(ax,50,40,34,14,'varie',label=r'absorbe $R\times I$',size='s')
box(ax,3,14,40,12,'resultat',label=r'4ℤ : 8 × 5 = 40 ∈ 4ℤ',size='s'); box(ax,45,14,40,12,'limite',label=r'1 ∉ 4ℤ : pas de 1',size='s')
arrow(ax,(23,30),(23,26),'fixe'); arrow(ax,(65,30),(65,26),'fixe')
text(ax,23,6,'idéal : oui','resultat','s'); text(ax,65,6,'sous-anneau : non','limite','s')
save(fig,'52-043')
