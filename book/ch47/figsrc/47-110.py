import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
d=6
text(ax,2,39+d,'(5 × 7) × 11','encre','s',ha='left'); text(ax,2,23+d,'5 × (7 × 11)','encre','s',ha='left')
box(ax,22,34+d,20,10,'sujet',label='5 × 7 → 11'); arrow(ax,(43,39+d),(46,39+d),'varie'); box(ax,47,34+d,21,10,'sujet',label='11 × 11 → 1')
box(ax,22,18+d,20,10,'autre',label='7 × 11 → 5'); arrow(ax,(43,23+d),(46,23+d),'varie'); box(ax,47,18+d,21,10,'autre',label='5 × 5 → 1')
arrow(ax,(69,39+d),(75,31+d),'resultat'); arrow(ax,(69,23+d),(75,27+d),'resultat')
box(ax,76,20+d,10,18,'resultat',label='classe\nde 1',size='s')
text(ax,44,d+10,'→ : reste modulo 12','fixe','s')
text(ax,2,4,'neutre','resultat','s',ha='left')
box(ax,22,0.5,64,8,'resultat',label=r'classe de 1 $\times$ classe de $x$ = classe de $x$',size='s')
save(fig,'47-110')
