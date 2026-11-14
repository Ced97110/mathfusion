import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 3, 84, 50, 'autre', dash=True)
text(ax, 44, 47, 'trace d’une algèbre (ch. 77)', 'autre', 'm')
box(ax, 8, 8, 72, 31, 'sujet')
text(ax, 44, 32, r"$T'$ : cas particulier", 'sujet', 'm')
text(ax, 44, 20, r'$(3+\sqrt{2})+(3-\sqrt{2})=6$', 'resultat', 'm')
save(fig, '66-144')
