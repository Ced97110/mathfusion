import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$a\leq b$ quand $a\vee b=b$','encre','m')
text(ax,22,52,'parties','resultat','m'); text(ax,66,52,'nombres, addition','limite','m')
box(ax,4,36,36,11,'resultat',label=r'$A\cup A=A$'); box(ax,48,36,36,11,'limite',label=r'$1+1=2$')
arrow(ax,(22,35),(22,27),'resultat'); arrow(ax,(66,35),(66,27),'limite')
box(ax,4,14,36,12,'resultat',label=r'$A\leq A$ : vrai'); box(ax,48,14,36,12,'limite',label=r'$1\leq1$ : faux')
save(fig,'80-153')
