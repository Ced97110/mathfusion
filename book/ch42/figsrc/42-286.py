import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
box(ax, 4, 22, 40, 24, 'sujet'); box(ax, 44, 22, 40, 24, 'autre')
for i, x in enumerate((12, 24, 36)): disc(ax, x, 34, 3.4, 'sujet', label=str(i + 1))
for i, x in enumerate((52, 64, 76)): disc(ax, x, 34, 3.4, 'autre', label=str(i + 4))
text(ax, 24, 52, r'$A$', 'sujet', 'l'); text(ax, 64, 52, r"$A'$", 'autre', 'l')
box(ax, 14, 2, 60, 14, 'resultat', label=r"$A\cap A'=\varnothing$" + "\naucun nombre dans les deux", size='s')
save(fig, '42-286')
