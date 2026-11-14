import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,56,'arrondi','varie','m'); text(ax,66,56,'radical exact','sujet','m')
box(ax,6,38,32,10,'varie',label='1,414'); box(ax,50,38,32,10,'sujet',label=r'$\sqrt{2}$')
arrow(ax,(22,38),(22,26),'encre'); arrow(ax,(66,38),(66,26),'encre')
text(ax,24,32,'au carré','encre','s',ha='left'); text(ax,68,32,'au carré','encre','s',ha='left')
box(ax,4,12,36,12,'limite',label='1,999396 ≠ 2'); box(ax,48,12,36,12,'resultat',label='2 exactement')
save(fig,'22-149')
